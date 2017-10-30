import sys
from apache_parser import apache_parser as Parser


class ApacheLogMapper():

    sysin = sys.stdin
    sysout = sys.stdout

    parser = Parser()

    def get_data(self):
        return self.sysin

    def save_data(self, host, request):
        self.sysout.write("{0}\t{1}\n".format(host, request))

    def parse(self):
        for line in self.get_data():
            data = self.parser.parse(line)
            if data is not None:
                self.save_data(data["host"], data["request"])


if __name__ == "__main__":
    alm = ApacheLogMapper()
    alm.parse()
