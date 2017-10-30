import unittest
import mock

from page_counter import PageCounter

class ApachePageCounter(unittest.TestCase):

    @mock.patch('page_counter.logging')
    def test_count_bad_lines(self, my_mock):
        page_counter = PageCounter()

        bad_line = 'this_is_a_bad_page'
        page_counter.add_line(bad_line)
        self.assertTrue(my_mock.log.called, "Bad Page Not Caught!")

    @mock.patch('page_counter.logging')
    def test_count_pages(self, my_mock):
        page_counter = PageCounter()
        for line in mock_lines:
            page_counter.add_line(line)
        self.assertTrue(len(page_counter.ranked_pages) == 3)
        self.assertTrue(page_counter.ranked_pages["/Page1"] == 3)
        self.assertTrue(page_counter.ranked_pages["/Page2"] == 2)
        self.assertTrue(page_counter.ranked_pages["/Page3"] == 1)
        self.assertFalse(my_mock.log.called, "Bad Page Caught, but should not have been!")

mock_lines = ['1.2.3.4  GET /Page1',
              '1.2.3.4  GET /Page1',
              '1.2.3.4  GET /Page2',
              '1.2.3.4  GET /Page3',
              '1.2.3.4  GET /Page2',
              '1.2.3.4  GET /Page1']

if __name__ == "__main__":
    suite = unittest.TestSuite()
    for method in dir(ApachePageCounter):
       if method.startswith("test"):
          suite.addTest(ApachePageCounter(method))
