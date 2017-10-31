#!/usr/bin/python
import sys


class ApacheLogReducer():

    sysin = sys.stdin
    sysout = sys.stdout

    def save_data(self, page, count):
        self.sysout.write("{0}\t{1}\n".format(page, count))
        self.sysout.flush

    def reduce(self, key):
        result = None
        page = ""
        currentPage = None
        count = 0

        for line in self.sysin:
            fields = line.split()
            ip = fields[-1]
            page = fields[0]
            if page != currentPage:
                if count > 0:
                    self.save_data(currentPage, count)
                    if key is not None and key in currentPage:
                        result = count
                currentPage = page
                count = 1
            else:
                count = count + 1

        # Don't forget the last page.
        self.save_data(page, count)
        return result

if __name__ == "__main__":
    reducer = ApacheLogReducer()
    reducer.reduce(None)
