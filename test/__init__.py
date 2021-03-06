"""
    test modules for the apl-py interpreter

    Test modules for apl-py are a combination of Python and Bash.  All are described here.

    - apl.py    a symbolic link to the real thing

    Python Unit Tests
    -----------------

    These are all doctest based.

    - dyadic.py                 exercise dyadic functions on numeric vectors

    - mixed.py                  exercise monadic and dyadic functions on mixed vectors

    - monadic.py                exercise monadic function on numeric vectors

    - nested.py                 exercise monadic and dyadic functions on nested vectors

    - parser.py                 exercise the parser (implemented in evaluate.py)

    - prototypes.py             check the 'array prototype' when a function return an empty vector

    - strings.py                exercise monadic and dyadic functions on character vectors

    - zilde.py                  exercise monadic and dyadic functions with empty vectors

    - base.py                   the bits common to all Python unit test modules extracted according
                                to the DRY principle.  It means all such modules accept the same
                                flags.

                                In practice it also includes routines that potentially might be
                                used in more than one test module.  In contradiction of the DRY
                                principle, the routine parseCommandLineArgs() is a clone of the
                                private routine by the same name found in apl.py

    APL Function-by-F
    unction Tests
    ------------------------------

    The alternative function-by-function tests allows the developer to run all tests for a given
    APL symbol, such as all the tests for ⍳.  These tests are implemented by a Bash script that
    creates and executes a special doctest module.  This modules runs the pertinent test functions
    from each of the Python unit test modules.

    - function                  Bash script that runs tests on a function-by-function basis.
                                See also:

                                    test/function --help

    - function.py               the template doctest module used by the 'function' script.

    - testFunction.py           the Python module generated and executed by the 'function' script.

    Bash Script Based Tests
    -----------------------

    In these tests the apl-py interpreter is run from a bash script, typically against a script
    containing APL statements, and the output is captured for comparison with a reference.

    - flags/run                 tests of CLI flags not covered by other run scripts

    - io/run                    tests of input and output using APL's ⎕ and ⍞ symbols

    - logs/run                  tests of logging session input and output

    - scripts/run               tests of executing APL commands from script files

    - framework                 another DRY section of code.  This time the bits common to all
                                Bash scripts named 'run' found in subdirectories.  It means all
                                such scripts have the same invocation.

                                The simplest invocation of a run script is:

                                    test/<subdir>/run

                                This will run all tests in <subdir> with pauses between each
                                (hit enter to continue) so the explanatory comments may be
                                read.  Use the -a flag to skip the pauses.

                                Some test cases enter the interactive interpreter.  You must
                                exit the interpreter manually (type ^D).  Such test cases may
                                be skipped by using -aa instead of -a.

                                The scripts are then fully automated but some test cases are
                                not executed.

                                The tests are split into sections that are numbered 1, 2, ...
                                By default the run script will execute all sections.  To
                                execute a subset, simply list them:

                                    test/<subdir>/run -aa 1 3 5

"""
