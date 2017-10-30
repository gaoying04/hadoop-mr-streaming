import sys
from page_counter import PageCounter
import operator

class ApacheLogReducer():

    sysin = sys.stdin
    sysout = sys.stdout

    pageCounter = PageCounter()

    def get_data(self):
        return self.sysin

    def save_data(self, page, count):
        self.sysout.write("{0}\t{1}\n".format(page, count))

    def reduce(self):
        for line in self.get_data():
            self.pageCounter.add_line(line)

        d = self.pageCounter.ranked_pages
        sorted_x = sorted(d.items(), key=lambda x: x[1])
        for page in sorted_x:
            self.save_data(page[0], self.pageCounter.ranked_pages[page[0]])


if __name__ == "__main__":
    alm = ApacheLogReducer()
    alm.reduce()
