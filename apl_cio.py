"""
    APL console input/output helper class

    UNDER DEVELOPMENT

    This is the ninth step of the transition.

    This step introduces the APL_fio class - a wrapper for a Python file handle

    The intention is that the complexities of console input and output will be
    delegated to the apl_cio module as and when it becomes advantageous to do so.
"""

import sys, readline, traceback

from apl_error import apl_quit

# ------------------------------

class   APL_fio (object):
    def __init__(self,mode):
        self.mode = mode
        self.handle = None
        self.path = None
        self.lineCount = 0

    def setPath (self,path):
        if self.handle is not None:
            self.handle.close()
            self.handle = None

        if path is not None:
            try:
                self.handle = open(path,self.mode)
                self.path = path
                self.lineCount = 0
            except:
                apl_quit(3,"unable to open '{0}' for {1}".format(path, "output" if self.mode == "w" else "input"))

    def fetchLine(self,closeOnEof=True):
        line = self.handle.readline()

        if line:
            self.lineCount += 1

            if self.lineCount == 1 and line.startswith("#!"):
                return self.fetchLine()

            return line.rstrip()

        if closeOnEof:
            self.setPath(None)

        raise(EOFError)

    def printString (self,string,end=None):
        if self.handle is not None:
            print(string,end=end,file=self.handle)

    def printTraceback (self, exc_type, exc_value, tb):
        if self.handle is not None:
            if exc_type is not None and exc_type != SystemExit:
                traceback.print_exception(exc_type,exc_value,tb,None,self.handle)

# ------------------------------

class   APL_cio (object):
    def __init__(self,prompt="",prefix=""):
        self.prompt = prompt
        self.prefix = prefix
        self.silent = False
        self.reset()
        self.scriptFile = APL_fio("r")
        self.inFile = APL_fio("r")
        self.outFile = APL_fio("w")
        self.logFile = APL_fio("w")
        self.sysin = APL_fio("r")
        self.sysout = APL_fio("w")
        self.sysout.handle = sys.stdout
        if not sys.stdin.isatty():
            self.sysin.path = "<stdin>"
            self.sysin.handle = sys.stdin

    def reset (self):
        self.newline = True
        self.prefixDone = False
        self.explicitPending = False
        self.hushExplicit = True
        self.hushImplicit = False
        self.userPromptLength = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.logFile.printTraceback(exc_type,exc_value,tb)
        self.scriptFile.setPath(None)
        self.inFile.setPath(None)
        self.outFile.setPath(None)
        self.logFile.setPath(None)

    def printStreams (self,streams,string,end=None):
        for stream in streams:
            stream.printString(string,end=end)

    def printResult (self,value):
        self.printStreams((self.sysout,),value)

    def printThis (self,value,end=None):
        self.printStreams((self.sysout,self.logFile),value,end)

    def printNewline (self):
        if self.outFile.handle is not None:
            self.printStreams((self.outFile,),"")
        elif self.silent:
            self.printThis("")

    def printImplicit (self,value):
        if self.hushImplicit:
            self.hushImplicit = False
        elif value is not None and not self.silent:
            if not self.prefixDone:
                self.printThis(self.prefix,end="")
                self.prefixDone = True

            self.printThis(value.resolve(),end='\n' if self.newline else '')

    def printExplicit (self,value):
        if value is not None:
            if not self.prefixDone and not self.silent:
                self.printThis(self.prefix,end="")
                self.prefixDone = True

            self.printStreams((self.sysout,self.logFile,self.outFile),value.resolve(),end='\n' if self.newline else '')

    def _errorInFile (self,fio,expr):
        if self.silent:
            self.printThis(self.prompt + expr)

        return " in {0} on line {1}".format(fio.path,fio.lineCount)

    def printError (self,fio,error,expr):
        if error.message:
            if fio is not None:
                if fio.handle is not None:
                    error.message += self._errorInFile(fio,expr)
                elif self.sysin.handle is not None:
                    error.message += self._errorInFile(self.sysin,expr)

            self.printThis('\r'+' '*(len(self.prompt)+expr.rfind(error.expr)),end="^\n")
            self.printThis(error.message)

    def read (self,fio):
        if fio.handle is not None:
            line = fio.fetchLine()

        elif self.sysin.handle is not None:
            line = self.sysin.fetchLine(False)

        else:
            self.printStreams((self.logFile,),self.prompt,end="")
            line = input(self.prompt)
            self.printStreams((self.logFile,),line)
            return line

        if not self.silent:
            self.printThis(self.prompt + line)

        if fio == self.inFile:
            if self.inFile.handle is not None:
                if self.outFile.handle is not None:
                    self.printStreams((self.outFile,),line)

        return line

# EOF
