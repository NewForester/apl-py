"""
    APL System Commands

    UNDER DEVELOPMENT

    This initial version implements only )OFF.
"""

from apl_error import apl_error, apl_exit

# ------------------------------

def     systemCommandOff(_, cio):
    """
    time to go ...
    """
    if not cio.silent:
        cio.printThis("Bye bye")
    apl_exit(0)

# ------------------------------

# a simple dictionary with (k, v) = (name, system-command-function)

_SystemCommands = {
    "OFF":      systemCommandOff,
}

# ------------------------------

def     systemCommand(name, arguments, cio):
    """
    invoke a system command

    the rest of the command line may be ignored
    """
    try:
        _SystemCommands[name.upper()](arguments.lstrip(), cio)
    except KeyError:
        apl_error("UNKNOWN SYSTEM COMMAND", name)

# EOF
