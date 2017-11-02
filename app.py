#!/usr/bin/env python

import sys, os
from slugify import Slugify

def main(txt):
    # Get stopwords
    path = os.path.dirname(os.path.realpath(__file__))
    file = open(path + '/stopwords.txt', 'r')
    stopwords = file.readline().split(',')

    # Init slugify
    slugify_url = Slugify()
    slugify_url.to_lower = True
    slugify_url.stop_words = list(stopwords)
    slug = slugify_url(txt)

    print slug
    return 0

def usage():
    print """
Usage: slugify <text to slugify>
"""
    return 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        usage()
