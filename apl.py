#!/usr/bin/python3
"""
    a simple implementation of APL in Python 3

    UNDER DEVELOPMENT

    This Python module is the executable command-line intepreter.

    For more information try:

                    apl.py --help
"""

import sys

from functools import reduce

from evaluate import evaluate_and_print

from apl_cio import APL_cio as apl_cio
from apl_error import APL_exception as apl_exception, apl_error, apl_exit, apl_quit

# ------------------------------

_banner = "APL Shell implemented in Python 3, Copyright 2017 NewForester"
_version = "Version 0.1.++, developed on Python 3.2.3"
_milestone = "Scalar calculator complete, vector calculator in progress"

_helpText = """
Invocation without any flags or arguments will enter an interactive APL shell.
Use an APL command such as )OFF to exit.

Invocation without flags but with arguments will interpret the arguments as
an APL expression, print the result and exit.  Eg:

    $ apl.py 4 8 16 ÷ 2
    2 4 8

Summary of the command line flags recognised by the interpreter:
    -l --log  <file>    log session input and output to <file>
    -f --file <file>    interpret contents of <file> as APL expressions
    -i --input <file>   redirect so that ⎕ and ⍞ are read from <file>
    -o --output <file>  record output from ⎕← and ⍞← in <file>

    -h --help           print this help text and exit
    -V --Version        print version information and exit

    -s --silent         suppress interactive output
    -v --verbose        resume interactive output

    --                  ends of flags (what follows are arguments, if any)

Note that at present in the interactive interpreter:

    ^C  (interrupt)     may be used to abort execution and quit the interpreter
    ^D  (end of input)  may be used to exit the interpreter instead of )OFF

This program is still under active development:  any and all features are
'as is' and subject to change.

Your curiosity is much appreciated. Thank you.



Logging and Scripting
---------------------

Logging and scripting is supported through command line flags.

It is possible to log the entire session to file:

    $ apl.py -l log_file

has the same effect as:

    $ apl.py |& tee -i log_file

except the second inconveniently disables readline editing.

Non-interactive (or scripted) use is supported:

    $ apl.py < script_file
    $ cat script_file | apl-py
    $ apl.py -f script_file

will all interpret script_file as a sequence of APL expressions.

APL allows for user functions to interact with the user explicitly via
the ⎕ and ⍞.  Such explicit input may be redirected using the -i flag:

    $ apl.py -i prompt_responses -f script_file

If the explicit input is not redirected in this way, user responses are
taken from standard input regardless of the use of the -f script_file.

In a similar fashion, explicit output may be redirected using the -o flag.
This redirection is independent of the use of the -l log_file flag.


Silent and Verbose Modes
------------------------

When using the interpreter interactively, by default, the interpreter issues
prompts and prints the results of evaluating individual APL expressions.

This output is generally not required in non-interactive mode and can be
turned off with the -s (or --silent) flag and on with the -v (or --verbose).

Silent mode does not turn off explicit output produced by ⎕ and ⍞ functions.
In silent mode, the contents of any -l log_file are almost identical to that of
a -o out_file but, should the interpreter crash, the former should contain a
Python call traceback, while the latter will not.

In silent mode, should apl-py raise an error (such as DOMAIN ERROR), then
silent mode will be broken in order to print an error message and diagnostics.

In script mode, apl-py will exit after reporting such an error and will not
attempt to interpret any further APL expressions.


Extended Script Modes
---------------------

The interpreter will exit whenever if encounters an )OFF command (or similar)
in a script.  This is the normal way of terminating an APL script.

If there is no )OFF command, the script file may be thought of an as rc file
needed to set up an appropriate working environment, perhaps by loading an
APL workspace.

If there are more command line flags, these are be processed so it is possible
to interpret several scripts one after the other.

    $ apl.py -f file_1 -f file_2 ...

If there are no more command line flags but there are arguments, the arguments
will be interpreted as a APL expression, the result printed and the interpreter
then will exit.

    $ apl.py -i white-mice -f hhgg -- askTheQuestion
    42

Otherwise, the interpreter will enter the interactive APL shell.


Executable Scripts
------------------

The "first line specifies the interpreter for the program" convention is
respected.  Make the script executable and ensure the first line reads:

    # !/usr/bin/apl.py --script -f

Use the path appropriate for your installation.  The -f flag must appear to the
right of any other flags.

This last detail gives rise to a small limitation.  As soon as the -f flag is
found, the contents of the script will be interpreted.  Thus any input file,
output file and log file must have already be specified.  Thus:

    $ apl.py -l log -o output -i input -f script

will work and do what is wanted but:

    $ apl.py -f script -l log -o output -i input

may also work but the log, output and input files will not be opened until the
last line in the script file has been interpreted, which is almost certainly
not what is wanted.

Similarly:

    $ executable_script -l log -o output -i input

will not give what is wanted but changing the first line of the executable
script to:

    # !/usr/bin/apl.py -l log -o output -i input -f

may not be satisfactory either.
"""

# ------------------------------

def     read_evaluate_print (cio):
    """
    read lines from a tty or a file, evaluate them and print the results
    """
    while True:
        cio.startNewLine()

        try:
            line = cio.read(cio.scriptFile)
        except EOFError:
            return

        try:
            evaluate_and_print(line,cio)
        except apl_exception as error:
            cio.printError(cio.scriptFile,error,line)
            if cio.scriptFile is not None:
                apl_exit(1)

# ------------------------------

if __name__ == '__main__':
    if len(sys.argv) == 1:
        flags, args = [], []
    elif '--' in sys.argv:
        ii = sys.argv.index("--")
        flags, args = sys.argv[1:ii], sys.argv[ii + 1:]
    elif sys.argv[1][0] == '-':
        flags, args = sys.argv[1:], []
    else:
        flags, args = [], sys.argv[1:]

    if len(flags):
        flags = ' '.join(flags).replace(' -',':-').split(':')

    try:
        with apl_cio(6 * ' ',"□") as cio:

            for flag in flags:
                if flag in ("-h", "--help"):
                    print(_banner)
                    apl_quit(0,_helpText)

                elif flag in ("-V", "--Version"):
                    print(_banner)
                    print(_version)
                    print(_milestone)
                    apl_quit(0)

            for flag in flags:
                if flag in ("-s", "--silent"):
                    cio.silent = True

                elif flag in ("-v", "--verbose"):
                    cio.silent = False

                elif flag.startswith(("-l ", "--log ")):
                    cio.logFile.setPath(flag.split()[1])

                elif flag.startswith(("-o ", "--output ")):
                    cio.outFile.setPath(flag.split()[1])

                elif flag.startswith(("-i ", "--input ")):
                    cio.inFile.setPath(flag.split()[1])

                elif flag.startswith(("-f ", "--file ")):
                    cio.scriptFile.setPath(flag.split()[1])
                    read_evaluate_print(cio)

                else:
                    apl_quit(3,"{0} not recognised: perhaps try --help".format(flag))

            if not sys.stdin.isatty():
                # stdin redirected

                read_evaluate_print(cio)

            elif not len(args):
                # enter interactive shell as there are is no command line expression

                cio.printThis(_banner)
                read_evaluate_print(cio)
                cio.printThis("^D")
                apl_exit(0)

            if len(args):
                # evaluate command line expression

                cio.prompt=""
                cio.prefix=""
                cio.silent=False
                cio.startNewLine()
                line = ' '.join(args)

                try:
                    evaluate_and_print(line,cio)
                    apl_exit(0)
                except apl_exception as error:
                    cio.printThis(line)
                    cio.printError(None,error,line)
                    apl_exit(1)

    except KeyboardInterrupt:
        apl_quit(2,"^C")

# EOF
