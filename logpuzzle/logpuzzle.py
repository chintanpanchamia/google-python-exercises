#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""


def read_urls(filename):
    """Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order."""
    # +++your code here+++
    f = open(filename, "rU")
    output = []
    for line in f:
        if("google-python-class" in line):
            match = re.search(r'(GET\s)([\S]+)(\sHTTP)', line)
            if(match.group(2) not in output):
                output.append(match.group(2))
            #print output
            print len(output)
    f.close()
    def sorter(url):
        match = re.search(r'[\w/.]+-(\w+)-(\w+).jpg', url)
        print match.group(2)
        return match.group(2)
    if 'animal' in filename:
        output = sorted(output)
        return output
    else:
        output = sorted(output, key=sorter)
        return output
    #print output



def download_images(img_urls, dest_dir):
    """Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    # +++your code here+++
    input = img_urls
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    n = 0
    p = os.path.abspath(dest_dir)
    f = open('index.html', 'w')
    f.write('<verbatim>\n')
    f.write('<html>\n')
    f.write('<body>\n')
    print "Downloading..."
    for link in img_urls:
        temp = dest_dir + '/img' + str(n) + '.jpg'
        url = 'http://code.google.com' + link
        urllib.urlretrieve(url, temp)
        f.write('<img src="'+ p +'/img'+ str(n) +'.jpg">')
        print 'img' + str(n)
        n += 1
    f.write('\n</body>')
    f.write('\n</html>')
    return



def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)


if __name__ == '__main__':
    main()
