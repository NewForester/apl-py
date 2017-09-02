"""
    APL console input/output helper classes

    UNDER DEVELOPMENT

    The classes in this module handle most of the complexity of `console i/o'.

    The complexity arises from the decision to implement logging and scripting
    in apl-py as well as the definition of APL's ⎕ and ⍞ functions.

    The current implementation is stable and less fragile that its predecessor.
    One of the reasons may be in the names:

    endOfLine, prefixDone, userPromptLength, newStmt record current state
    ('what has happened')

    hushImplicit records future state ('what must be done')
"""

import sys
import readline
import traceback

from aplQuantity import aplQuantity
from aplError import aplException, aplQuit

# ------------------------------

def     _notesOnStreams():
    """
    The interpreter considers console i/o to involve four streams:
    - in - APL expressions to evaluate
    - out - prompts and results
    - out - ⎕← and ⍞← explicit prompts and results
    - in - ⎕ and ⍞ data and responses in

    For normal interactive use, these default to sysin and sysout.

    These six streams are represented by members of the aplCio object that are
    themselves objects of this class.  Output is an 'and' - potentially sysout
    and logFile and outFile while input is an 'or' - either scriptFile or
    inFile, if defined, or otherwise sysin.

    The main complication on input streams is ensuring input and prompts are
    echoed to output streams appropriately.  The main complication for output
    streams is taking advantage of Python iterators types.
    """
    pass

def     _notesOnConsoleIO():
    """
    Console i/o is 'encapsulated' in a single object of type aplCio passed up,
    as well as down, the recursive call tree that is the parser implemented in
    evaluate.py.

    The flags passed to apl-py on invocation determine the initial and largely
    static state of the object and other state variables are set and reset at
    different points in evaluate.py ('side-effects').

    The object is passed to systemCommands.py but solely to determine whether
    or not to print messages such "Bye bye" as part of the )OFF command.

    The ⎕ input operator involves invoking the parser from the top-level.  The
    aplCio object is cloned and the clone passed to this second 'instance' of
    the parser so that the state passed back up the call stack is known.
    """
    pass

def     _notesOnComplications():
    """
    The complications for dealing with edge cases that arise with ⎕ and ⍞ are
    less straight forward (aka ugly and not easy to 'reason about').

    It seems most arise from the need to support lines of the form:

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

    prints the value of A once, not twice.  The explicit, intermediary result
    is printed and the printing of the final result is suppressed.  Look for
    the hushImplicit flag.

    The final result is also not printed when the left hand end of the
    expression is an assignment or the stop function:

        A← 1
        ⊣ 2

    The ⍞← operator prints without a new line but the interpreter has to ensure
    a new line is printed at the end of the final result before printing the
    prompt for the next line of input.  See the endOfLine member variable.

    The final Byzantine element in all this is userPromptLength.  The width of
    "What is your name ? " is remembered and NAME is prefixed with a string of
    this length.  Some implementations prefix the prompt, others prefix spaces.
    The apl-py implementation prefixes spaces.

    The need to support userPromptLength forces state to be carried forward
    between expressions on the same line.  It was the straw that led the camel
    to implement aplCio.
    """
    pass

# ------------------------------

class   aplSio(object):
    """
    a simple wrapper for an i/o stream (aka file handle)
    """
    def __init__(self, mode):
        self.mode = mode
        self.handle = None
        self.path = None
        self.lineCount = 0

    def setPath(self, path):
        """
        (re)set the stream's file systen, closing and reopening the stream as necessary
        """
        if self.handle is not None:
            self.handle.close()
            self.handle = None

        if path is not None:
            try:
                self.handle = open(path, self.mode)
                self.path = path
                self.lineCount = 0
            except IOError:
                mode = "output" if self.mode == "w" else "input"
                aplQuit(3, "unable to open '{0}' for {1}".format(path, mode))

    def fetchLine(self, closeOnEof=True):
        """
        read a line of input from the stream, keep track of the line number and signal end-of-file
        """
        line = self.handle.readline()

        if line:
            self.lineCount += 1

            if self.lineCount == 1 and line.startswith("#!"):
                return self.fetchLine()

            return line.rstrip()

        if closeOnEof:
            self.setPath(None)

        raise EOFError

    def printString(self, string, end=None):
        """
        print a string to the stream
        """
        if self.handle is not None:
            print(string, end=end, file=self.handle)

    def printTraceback(self, exceptionType, exceptionValue, traceBack):
        """
        print Python trace back to the stream
        """
        if self.handle is not None and exceptionType is not None and exceptionType != SystemExit:
            traceback.print_exception(exceptionType, exceptionValue, traceBack, None, self.handle)

# ------------------------------

def     _outputString(streams, string, end=None):
    """
    print a string to one or more streams
    """
    for stream in streams:
        stream.printString(string, end=end)

# ------------------------------

class   _outputValue(object):
    """
    print, prettily, an APL quantity, to one or more streams
    """
    def __init__(self, streams, quantity, end=None):
        self._streams = streams
        self._printed = 0

        self._outputQuantity(quantity, end)

    def _output(self, string, end):
        """
        print a string and update the count of characters printed so far on this line
        """
        if not string is None:
            for stream in self._streams:
                stream.printString(string, end=end)

            self._printed += len(string)

            if end is None or end == '\n':
                self._printed = 0
            else:
                self._printed += len(end)

    def _outputQuantity(self, quantity, end):
        """
        print an APL quantity recursively
        """
        try:
            string = None
            separator = ''

            if quantity.isEmptyVector():
                string = '⍬' if quantity.prototype() == 0 else ''
            else:
                for element in quantity:
                    if isinstance(element, str):
                        self._output(string, separator)

                        string = element
                        separator = ''

                    elif isinstance(element, aplQuantity):
                        separator = ' '
                        self._output(string, separator)

                        if element.isVector():
                            outfix = "'"  if element.isString() else '('
                            self._output(outfix, '')

                        self._outputQuantity(element, '')
                        string = ''

                        if element.isVector():
                            outfix = "'"  if element.isString() else ')'
                            self._output(outfix, '')

                    else:
                        separator = ' '
                        self._output(string, separator)

                        string = "{0:.10g}".format(element)
                        string = "0" if string == "-0" else string.replace('-', '¯')

            self._output(string, end)

        except aplException as error:
            if not error.expr:
                error.expr = quantity.expressionToGo
            if self._printed != 0:
                _outputString(self._streams, '\b \b'*self._printed, end='')
                self._printed = 0
            raise error

# ------------------------------

class   aplCio(object):
    """
    a representation of console i/o
    """
    def __init__(self, prompt="", prefix=""):
        self.prompt = prompt
        self.prefix = prefix
        self.silent = False
        self.scriptFile = aplSio("r")
        self.inFile = aplSio("r")
        self.outFile = aplSio("w")
        self.logFile = aplSio("w")
        self.sysin = aplSio("r")
        self.sysout = aplSio("w")
        self.sysout.handle = sys.stdout
        if not sys.stdin.isatty():
            self.sysin.path = "<stdin>"
            self.sysin.handle = sys.stdin
        self.endOfLine = '\n'
        self.prefixDone = False
        self.userPromptLength = 0
        self.newStmt = True
        self.hushImplicit = self.silent

    def startNewLine(self):
        """
        reset state variables at the start of a new line of APL
        """
        self.endOfLine = '\n'
        self.prefixDone = False
        self.userPromptLength = 0
        self.startNewStmt()

    def startNewStmt(self):
        """
        reset state variables at the start of an APL expression
        """
        self.newStmt = True
        self.hushImplicit = self.silent

    def __enter__(self):
        """
        called at the start a Python with block (to ensure streams are closed)
        """
        return self

    def __exit__(self, exceptionType, exceptionValue, traceBack):
        """
        called at the end of a Python with block (to close any open streams)
        """
        self.logFile.printTraceback(exceptionType, exceptionValue, traceBack)

        self.scriptFile.setPath(None)
        self.inFile.setPath(None)
        self.outFile.setPath(None)
        self.logFile.setPath(None)

    def printString(self, string, end=None):
        """
        print a string - not the value of an APL quantity
        """
        _outputString((self.sysout, self.logFile), string, end)

    def printResult(self, value):
        """
        format and print the result of evaluating a test expression
        """
        _outputValue((self.sysout,), value)

    def printEndOfLine(self):
        """
        print \n at end of line evaluation following output with ⍞
        """
        if self.endOfLine != '\n':
            if self.hushImplicit:
                _outputString((self.sysout, self.logFile, self.outFile), "")
            else:
                _outputString((self.outFile,), "")

    def printImplicit(self, value):
        """
        print an implicit result (not one passed to ⎕ or ⍞)
        """
        if value is not None and not self.hushImplicit:
            if not self.prefixDone:
                self.printString(self.prefix, end="")
                self.prefixDone = True

            _outputValue((self.sysout, self.logFile), value)
            self.endOfLine = '\n'

    def printExplicit(self, value, end='\n'):
        """
        print an explicit result (one passed to ⎕ or ⍞)
        """
        if value is not None:
            if not self.prefixDone and not self.silent:
                self.printString(self.prefix, end="")
                self.prefixDone = True

            _outputValue((self.sysout, self.logFile, self.outFile), value, end=end)
            self.endOfLine = end

    def _errorInFile(self, sio, expr):
        """
        return where in an input script an error occurred (and print the offending line)
        """
        if self.silent:
            self.printString(self.prompt+expr)

        return " in {0} on line {1}".format(sio.path, sio.lineCount)

    def printError(self, sio, error, expr):
        """
        print an error message and error diagnostics
        """
        if error.message:
            if sio is not None:
                if sio.handle is not None:
                    error.message += self._errorInFile(sio, expr)
                elif self.sysin.handle is not None:
                    error.message += self._errorInFile(self.sysin, expr)

            self.printString('\r'+' '*(len(self.prompt)+expr.rfind(error.expr)), end="^\n")
            self.printString(error.message)

    def read(self, sio):
        """
        read a line of input from the preferred stream (sio)

        otherwise fall back to redirected stdin or else the console

        echo to log and output files as appropriate
        """
        if sio.handle is not None:
            line = sio.fetchLine()

        elif self.sysin.handle is not None:
            line = self.sysin.fetchLine(False)

        else:
            _outputString((self.logFile,), self.prompt, end="")
            line = input(self.prompt)
            _outputString((self.logFile,), line)
            return line

        if not self.silent:
            self.printString(self.prompt+line)

        if sio == self.inFile:
            if self.inFile.handle is not None:
                if self.outFile.handle is not None:
                    _outputString((self.outFile,), line)

        return line

# EOF
