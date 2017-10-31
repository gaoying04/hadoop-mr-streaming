import logging
import re

logging.basicConfig(filename='parser.log', level=logging.DEBUG)

class apache_parser:

    def parse(self, line):
        try:
            p = re.compile(
                '([^ ]*) ([^ ]*) ([^ ]*) \[([^]]*)\] "([^"]*)" ([^ ]*) ([^ ]*)'
            )
            m = p.match(line)
            host, user, client, server_time, request, status, size = m.groups()
            result = {'host': host, 'user': user, 'client': client, 'time': server_time, 'request': request, 'status': status, 'size': size}
            return result

        except Exception:
            logging.log(logging.WARNING, "Error parsing line.")
            return None
