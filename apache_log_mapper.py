#!/usr/bin/python
import logging
import sys
sys.path.append('./')

from apache_parser import apache_parser as Parser

# logging.basicConfig(filename='mapper.log', level=logging.DEBUG)

# sysin = sys.stdin
# sysout = sys.stdout
parser = Parser()


# def save_data(request, host):
#    print("{0}\t{1}".format(request.split()[1], host))


#def parse():
#    logging.debug("Starting mapper job")
try:
    for line in sys.stdin:
        data = parser.parse(line)
        if data is not None:
            print("{0}\t{1}".format(data["request"], data["time"]))
except Exception as ex:
    logging.error("An error has occurred:\n{0}\n".format(ex.message))
finally:
    logging.debug("Mapping complete. Closing local mapper log file.")

#Do the work
# parse()