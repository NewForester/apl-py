#!/usr/bin/python3
"""
    A simple wrapper script for the APL Read-Evaluate-Print loop
"""

from rep import read_evaluate_print, apl_quit

if __name__ == '__main__':
    print("APL Read-Evaluate-Print Loop.")
    try:
        read_evaluate_print ('       ')
    except KeyboardInterrupt:
        apl_quit()

# EOF
