#!/usr/bin/env python
import os
import sys
import argparse as ap


def is_valid_file(arg):
    if os.path.isfile(arg):
        return os.path.abspath(arg)
    else:
        raise ap.ArgumentTypeError(
                'Specified path does not exist or is not a file')


parser = ap.ArgumentParser(description='Open a website or file in chrome')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-w', '--web_url', metavar='WEB URL',
                   help='The url of the web page to be opened')
group.add_argument('-f', '--file', type=is_valid_file, metavar='FILE',
                   help='The path of the local file to be opened')
args = parser.parse_args()

url = "https://{}".format(args.web_url) if args.web_url else args.file
os.system("open -a Google\ Chrome {}".format(url))
