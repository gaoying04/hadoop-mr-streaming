import logging


class PageCounter:

    ranked_pages = dict()

    def add_line(self, line):
        try:
            fields = line.split()
            ip = fields[0]
            page = fields[-1]
            if page[0]!='/':
                page = fields[-2]
            if len(fields) < 2 :
                logging.log(logging.WARN, "Unable to count page.  Dropping it on the floor.")
                logging.log(page)
                return None
            self.add_page(page)
        except Exception:
            logging.log(logging.WARN, "Unable to count page.  Dropping it on the floor.")

    def add_page(self, page):
        if page in self.ranked_pages.keys():
            self.ranked_pages[page] = self.ranked_pages[page] + 1
        else:
            self.ranked_pages[page] = 1
