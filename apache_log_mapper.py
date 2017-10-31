#!/usr/bin/python
import logging
import sys
sys.path.append('./')

from apache_parser import apache_parser as Parser

logging.basicConfig(filename='mapper.log')


class ApacheLogMapper():

    sysin = sys.stdin
    sysout = sys.stdout

    parser = Parser()

    def save_data(self, request, host):
        self.sysout.write("{0}\t{1}\n".format(request.split()[1], host))
        self.sysout.flush()

    def parse(self):
        print("Got to here!")
        logging.debug("Starting mapper job")
        try:
            for line in self.sysin:
                data = self.parser.parse(line)
                if data is not None:
                    self.save_data(data["request"], data["time"])
        except Exception as ex:
            logging.error("An error has occurred:\n{0}\n".format(ex.message))
        finally:
            logging.debug("Mapping complete. Closing local mapper log file.")

#Do the work
if __name__ == "__main__":
    mapper = ApacheLogMapper()
    mapper.parse()
