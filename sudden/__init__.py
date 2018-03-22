#!/usr/bin/env python3

import argparse

from sudden.sudden import Sudden

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--update', dest='update', action='store_true')
parser.add_argument('-i', dest='tool', required=False, nargs='+', metavar='conda', help='any tool to be installed')

# args = parser.parse_args()
# print(args)
# print('hell')
#
# s = Sudden()

# if args.update:
#     s.update()
# if args.tool:
# 	s.install(args.tool)