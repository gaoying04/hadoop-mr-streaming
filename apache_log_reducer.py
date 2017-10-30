import sys
from page_counter import PageCounter

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

        for page in self.pageCounter.ranked_pages:
            self.save_data(page, self.pageCounter.ranked_pages[page])


if __name__ == "__main__":
    alm = ApacheLogReducer()
    alm.reduce()
