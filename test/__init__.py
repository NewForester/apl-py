"""
    test modules for the apl-py interpreter

    Test modules for apl-py are a combination of Python and Bash.  All are
    described here.

    - apl.py    a symbolic link to the real thing

    - base.py   the bits common to all Python test modules extracted according
                to the DRY principle.  It means all such modules accept the
                same flags.

                In practice it also includes routines that potentially might be
                used in more than one test module.  In contradiction of the DRY
                principle, the routine parseCommandLineArgs() is a clone of the
                private routine by the same name found in apl.py

    - framework another DRY section of code.  This time the bits common to all
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

    - flags/run         tests of CLI flags not covered by other run scripts

    - io/run            tests of redirecting input and output

    - logs/run          tests of logging session input and output

    - scripts/run       tests of executing APL commands from script files

"""