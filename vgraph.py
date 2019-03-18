#!/bin/env python

"""Show a sparkline graph given a floating point number between 0.0 and 1.0
(inclusive)."""

import sys


def print_usage(message=None):
    """Print command-line usage to `stderr` and exit."""
    if message is not None:
        sys.stderr.write(f"Error: {message!s}\n")
    sys.exit(f"""Usage: {sys.argv[0]} NUMBER [NUMBER ...]""")


def main(argv):
    """Pass numbers to `main` to print as a graph."""
    if len(argv) > 1:
        arg = argv[1]
    else:
        print_usage()

    try:
        arg = float(arg)
        arg = round(float(arg) * 8.0)
        if not 0 <= arg <= 8:
            raise ValueError("Number must be between 0.0 and 1.0 (inclusive)")
    except ValueError as err:
        print_usage(err)

    print(arg)


if __name__ == "__main__":
    main(sys.argv)
