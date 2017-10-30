import sys

class ApacheLogReducer():

    sysin = sys.stdin
    sysout = sys.stdout

    def get_data(self):
        return self.sysin

    def save_data(self, page, count):
        self.sysout.write("{0}\t{1}\n".format(page, count))

    def reduce(self):
        page = ""
        currentPage = None
        count = 0
        for line in self.get_data():
            fields = line.split()
            ip = fields[-1]
            page = fields[0]
            if page != currentPage:
                if count > 0:
                    self.save_data(page, count)
                currentPage = page
                count = 1
            else:
                count = count + 1

        # Don't forget the last page.
        self.save_data(page, count)

if __name__ == "__main__":
    alm = ApacheLogReducer()
    alm.reduce()
