#!/usr/bin/env python3

"""
Stanford CS106A TipTop Project
"""

import sys


# define functions here
def read_tags(filename):
    tags = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            parts = line.split('^')
            # ['@alice', '#meh', '#bleh', '#NOPE', ...]
            posters = parts[0].lower()
            list_otag = parts[1:]
            for tag in list_otag:
                low_tag = tag.lower()
                if low_tag not in tags:
                    tags[low_tag] = []
                if posters.lower() not in tags[low_tag]:
                    tags[low_tag].append(posters)
    return tags


def report(tags):
    for tag in sorted(tags.keys()):
        print(tag)
        for poster in sorted(tags[tag]):
            print(' ' + poster)


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        tags = read_tags(args[0])
        report(tags)


if __name__ == '__main__':
    main()
