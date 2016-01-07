#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(direc):
    paths = os.listdir(direc)
    output = []
    for names in paths:
        match = re.search(r'__(\w)+__', names)
        if match.group() != "":
            output.append(os.path.abspath(os.path.join(direc, names)))
    return output

def copy_to(paths, direc):
    if not os.path.exists(direc):
        os.mkdir(direc)
    for path in paths:
        fname = os.path.basename(path)
        dest = os.path.join(direc, fname)
        shutil.copy(path, dest)

def zip_to(paths, zip):
    cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
    print cmd
    (status, output) = commands.getstatusoutput(cmd)
    if status:
        sys.stderr.write(output)
        sys.exit(1)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    todir = ''
    tozip = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
    elif args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]



    output = []
    for dirname in args:
        output.extend(get_special_paths(dirname))

    if todir:
        copy_to(output, todir)
    elif tozip:
        zip_to(output, tozip)


if __name__ == "__main__":
    main()
