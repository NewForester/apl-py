"""
    The top level of the APL Read-Evaluate-Print loop

    UNDER DEVELOPMENT

    This version simply echoes user input and exits on end-of-input
"""

def     read_evaluate_print (prompt):
    """
    Read input, echo input
    """
    try:
        while True:
            print(end=prompt)
            line = input()
            print('⎕', line)
    except EOFError:
        print()

# EOF
