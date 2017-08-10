"""
Common twitter specific functions.
"""

def list_to_csv(args):
    """
    Convert a list to a string csv.
    """

    args = map(str, args)
    args = ",".join(args)
    return args
