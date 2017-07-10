"""
    APL System Commands

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done
"""

from apl_error import apl_error, apl_exit

# ------------------------------

def     sys_cmd_off (arguments,cio):
    """
    time to go ...
    """
    if not cio.silent:
        cio.printThis("Bye bye")
    apl_exit(0)

# ------------------------------

system_commands = {
    "OFF":      sys_cmd_off,
}

# ------------------------------

def     system_command (name,arguments,cio):
    """
    invoke a system command

    the rest of the command line may be ignored

    throws UNKNOWN SYSTEM COMMAND if the name is not recognised
    """
    try:
        system_commands[name.upper()](arguments.lstrip(),cio)
    except KeyError:
        apl_error("UNKNOWN SYSTEM COMMAND", name)

# EOF
