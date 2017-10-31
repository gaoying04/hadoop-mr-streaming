import sys
from apache_parser import apache_parser as Parser


class ApacheLogMapper():

    local_log = None

    def __init__(self):
        self.local_log = open("mapper_logfile", "w")

    sysin = sys.stdin
    sysout = sys.stdout

    parser = Parser()

    def get_data(self):
        return self.sysin

    def save_data(self, request, host):
        self.sysout.write("{0}\t{1}\n".format(request.split()[1], host))
        self.sysout.flush()
        return

    def parse(self):
        self.local_log.write("Starting mapper job")
        try:
            for line in self.get_data():
                data = self.parser.parse(line)
                if data is not None:
                    self.save_data(data["request"], data["time"])
        except Exception as ex:
            self.local_log.write("An error has occurred:\n{0}\n".format(ex.message))
        finally:
            self.local_log.write("Mapping complete. Closing local mapper log file.")
            self.local_log.flush()
            self.local_log.close()

if __name__ == "__main__":
    alm = ApacheLogMapper()
    alm.parse()
