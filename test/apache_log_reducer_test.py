from apache_log_reducer import ApacheLogReducer as Reducer
import unittest
import mock


class ApacheLogMapperTest(unittest.TestCase):

    @mock.patch('page_counter.PageCounter')
    def test_mapper_can_parse_from_standard_in(self, my_mock):
        reducer = Reducer()
        reducer.pageCounter = my_mock
        reducer.sysin = open('../data/reducer_fixture','r')
        reducer.reduce()
        self.assertTrue(my_mock.add_line.called, "Failed to call the add line method!")

    @mock.patch('sys.stdout')
    def test_mapper_can_save_data(self, my_mock):
        reducer = Reducer()
        reducer.sysin = open('../data/reducer_fixture', 'r')
        reducer.sysout = my_mock
        reducer.reduce()
        self.assertTrue(my_mock.write.called, "Failed to output data message.")