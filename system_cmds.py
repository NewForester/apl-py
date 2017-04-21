"""
    APL System Commands

    UNDER DEVELOPMENT

    This is an initial version:  there is much still to be done
"""

from apl_exception import APL_Exception as apl_exception, apl_exit

# ------------------------------

def     sys_cmd_off (arguments):
    """
    time to go ...
    """
    apl_exit("Bye bye")

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
        raise (apl_exception("UNKNOWN SYSTEM COMMAND", name))

# EOF
