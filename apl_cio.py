"""
    APL console input/output helper classes

    UNDER DEVELOPMENT

    This is the ninth step of the transition.

    This step introduces the APL_fio class - a wrapper for a Python file handle.

    It also represents the first attempt to document the mess.
"""
"""
    The classes declared in this module handle most of the complexities of
    `console i/o'.  The complexity arises partly from the decision to implement
    logging/scripting capabilities in apl-py and partly from the definition of
    APL's ⎕ and ⍞ functions.

    The behaviour is 'encapsulated' in a single object of type APL_cio that is
    passed up as well as down the recursive call tree in the parser implemented
    in evaluate.py.  The flags passed to apl-py on invocation determine the
    initial (static) state of the object and other state variables are set and
    cleared at different points in evaluate.py ('side-effects').

    The object is passed to system_cmds.py to determine whether or not to print
    messages such "Bye bye" as part of processing the )OFF command.

    The ⎕ input operator involves invoking the parser from the top-level.  The
    APL_cio object is cloned and the clone passed to this second 'instance' of
    the parser so that the state passed back up the call stack is known.
"""
"""
    The interpreter considers console i/o to involve four streams:
        - in - APL expressions to evaluate
        - out - prompts and results
        - out - ⎕← and ⍞← explicit prompts and results
        - in - ⎕ and ⍞ data and responses in

    For normal interactive use, these degenerate into sysin and sysout.

    These six streams are represented by members of the APL_cio object that are
    represented by objects of class APL_fio.  Output is an 'and' - potentially
    sysout and logFile and outFile while input is an 'or' - either scriptFile
    or inFile, if defined, otherwise sysin.

    The main complication on input streams is ensuring input and prompts are
    echoed to output streams appropriately.  The main complication for output
    streams is taking advantage of Python iterators types.
"""
"""
    The complications for dealing with edge cases that arise with ⎕ and ⍞ are
    less straight forward (aka ugly and not easy to 'reason about').

    It seems that most, if not all, of the complications arise from the need to
    support lines of the form:

        ⍞← "What is your name ? " ⋄ NAME ←⍞

    with no newline printed between the prompt and the response.

    For simple interactive use, an expression is evaluated and the result is
    printed.  Simple.

    The first complication is the expression separator ('⋄').  APL expression
    evaluation is simple as long as the strict right-to-left evaluation rule
    holds.  The expression separator introduces a left-to-right evaluation of
    the individual expressions.  This anomalous behaviour is handled in
    evaluate::evaluate_and_print().

    The expression separator complicates console i/o since results are output
    on a expression-by-expression a basis but default prompts are output on a
    line-by-line basis.  Look for the prefixDone flag.

    The ⎕← and ⍞← operators print intermediary results.  The first complication
    for console i/o is that a simple expression such as:

        ⎕← A

    prints the value of A once, not twice.  It would seem sensible in such
    circumstances to print the explicit, intermediary result and suppress
    the printing of the final result but the opposite has been implemented.
    Look for the hushExplicit and explicitPending.

    This may have been the inferior choice.  The choice was made in order to
    handle a further complication.  The ⍞← operator prints without a new line
    but the interpreter has to ensure newlines are printed between each line of
    of input.  See the newline (and newlinePending) flags.

    The final Byzantine element in all this is userPromptLength.  The width of
    "What is your name ? " is remembered and NAME is prefixed with a string of
    this length.  Some implementations prefix the prompt, others prefix spaces.
    This implementation prefixes spaces.

    The need to support userPromptLength forces state to be carried forward
    between expressions on the same line.  It was the straw that led the camel
    to implement APL_cio.
"""
"""
    The current implementation is stable but fragile.  One of the reasons may
    be in the names:

        prefixDone and userPromptLength record past state ('what has happened')

        newline, explicitPending, hushExplicit, hushImplicit record future
        state ('what must be done')

    Changing the state variable to record what has happened may yield a more
    reasonable implementation.
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
