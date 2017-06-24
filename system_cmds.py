"""
    APL System Commands

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done
"""

from apl_error import apl_error, apl_exit

# ------------------------------

def     sys_cmd_off (arguments):
    """
    time to go ...
    """
    apl_exit(0,"\bBye bye")

# ------------------------------

system_commands = {
    "OFF":      sys_cmd_off,
}

# ------------------------------

def     system_command (name,arguments):
    """
    invoke a system command

    the rest of the command line may be ignored

    throws UNKNOWN SYSTEM COMMAND if the name is not recognised
    """
    try:
        system_commands[name.upper()](arguments.lstrip())
    except KeyError:
        apl_error("UNKNOWN SYSTEM COMMAND", name)

# EOF
