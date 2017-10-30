from apache_parser import apache_parser as Parser

import unittest
import mock


class TestApacheParser(unittest.TestCase):

    @mock.patch('apache_parser.logging')
    def test_parse_invalid_line(self, my_mock):
        parser = Parser()

        result = parser.parse("stuff")
        self.assertTrue(my_mock.log.called, "Failed to log an error message.")
        self.assertTrue(result is None)

    @mock.patch('apache_parser.logging')
    def test_valid_line(self, my_mock):
        parser = Parser()

        result = parser.parse('10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469')

        self.assertTrue(len(result) == 7)
        self.assertTrue(result["host"] == '10.223.157.186')
        self.assertTrue(result["user"] == '-')
        self.assertTrue(result["client"] == '-')
        self.assertTrue(result["time"] == '15/Jul/2009:15:50:35 -0700')
        self.assertTrue(result["request"] == 'GET /assets/js/lowpro.js HTTP/1.1')
        self.assertTrue(result["status"] == '200')
        self.assertTrue(result["size"] == '10469')

        self.assertFalse(my_mock.log.called, "Logged error when none should have been logged.")


if __name__ == '__main__':
    unittest.main()