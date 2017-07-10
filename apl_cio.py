"""
    APL console input/output helper class

    UNDER DEVELOPMENT

    This is the eigth step of the transition.

    This step adds support for logging an apl.py session.

    The intention is that the complexities of console input and output will be
    delegated to the apl_cio module as and when it becomes advantageous to do so.
"""

import readline
import traceback

# ------------------------------

class   APL_cio (object):
    def __init__(self,prompt="",prefix=""):
        self.prompt = prompt
        self.prefix = prefix
        self.silent = False
        self.fileInput = False
        self._logFile = None
        self.reset()

    def reset (self):
        self.newline = True
        self.prefixDone = False
        self.hushExplicit = True
        self.hushImplicit = False
        self.userPromptLength = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if self._logFile is not None:
            if exc_type is not None and exc_type != SystemExit:
                traceback.print_exception(exc_type,exc_value,tb,None,self._logFile)
        self.logFile(None)

    def logFile (self,path):
        if self._logFile is not None:
            self._logFile.close()
            self._logFile = None
        if path is not None:
            self._logFile = open(path,"w")

    def printThis (self,string,end=None):
        print(string,end=end)
        if self._logFile is not None:
            print(string,end=end,file=self._logFile)

    def printResult (self,value):
        self.printThis(value)

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

            self.printThis(value.resolve(),end='\n' if self.newline else '')

    def printError (self,error,expr,where=""):
        if error.message:
            self.printThis('\r'+' '*(len(self.prompt)+expr.rfind(error.expr)),end="^\n")
            self.printThis(error.message + where)

    def inputAndLog (self):
        if self._logFile is not None:
            print(self.prompt,end="",file=self._logFile)

        line = input(self.prompt)

        if self._logFile is not None:
            print(line,file=self._logFile)

        return line
# EOF
