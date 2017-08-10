"""
    APL System Commands

    UNDER DEVELOPMENT

    This initial version implements only )OFF.
"""

from aplError import aplError, aplExit

# ------------------------------

def     systemCommandOff(_, cio):
    """
    time to go ...
    """
    if not cio.silent:
        cio.printString("Bye bye")
    aplExit(0)

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
        aplError("UNKNOWN SYSTEM COMMAND", name)

# EOF
