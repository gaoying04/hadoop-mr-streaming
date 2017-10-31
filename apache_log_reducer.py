#!/usr/bin/python
import sys


sysin = sys.stdin
sysout = sys.stdout

def save_data(page, count):
    print("{0}\t{1}".format(page, count))

def reduce():
    page = ""
    currentPage = None
    count = 0

    for line in sysin:
        fields = line.split()
        ip = fields[-1]
        page = fields[0]
        if page != currentPage:
            if count > 0:
                save_data(currentPage, count)
            currentPage = page
            count = 1
        else:
            count = count + 1

    # Don't forget the last page.
    save_data(page, count)

#Do the work here...
reduce()