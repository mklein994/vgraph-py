#!/bin/env python

import sys


def print_usage():
    sys.exit(f"""Usage: {sys.argv[0]} NUMBER [NUMBER ...]""")


a = None
if len(sys.argv) > 1:
    a = sys.argv[1]
else:
    print_usage()

print(a)
