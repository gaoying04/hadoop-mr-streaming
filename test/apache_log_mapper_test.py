from apache_log_mapper import ApacheLogMapper as Mapper
import unittest
import mock


class ApacheLogMapperTest(unittest.TestCase):

    @mock.patch('apache_parser.apache_parser')
    def test_mapper_can_parse_from_standard_in(self, my_mock):
        mapper = Mapper()
        mapper.parser = my_mock
        mapper.sysin = open('../data/access_log_test_fixture','r')
        mapper.parse()
        self.assertTrue(my_mock.parse.called, "Failed to call the parser!")

    @mock.patch('sys.stdout')
    def test_mapper_can_save_data(self, my_mock):
        mapper = Mapper()
        mapper.sysin = open('../data/access_log_test_fixture', 'r')
        mapper.sysout = my_mock
        mapper.parse()
        self.assertTrue(my_mock.write.called, "Failed to output data message.")