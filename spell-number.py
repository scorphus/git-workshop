#!/usr/bin/env python
import sys

from numbers import spell_number

if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(spell_number(n) or '?')
