import unittest
import builtins
from unittest.mock import patch, call
from importlib import reload

class TestDashes(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.return_value = 'Programming 1'
        import dashes
        reload(dashes)
        input_call.assert_called_once
        input_call.assert_called_with('Enter text: ')
        print_call.assert_called_once
        print_call.assert_called_with('-P-r-o-g-r-a-m-m-i-n-g- -1-')

class TestPatterns(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.return_value = '4'
        import patterns
        reload(patterns)
        input_call.assert_called_once
        input_call.assert_called_with('Enter a number to generate a cool pattern: ')
        self.assertEqual(4, print_call.call_count)
        print_calls = print_call.call_args_list
        self.assertEqual(print_calls[0].args[0], '1 2 3 4')
        self.assertEqual(print_calls[1].args[0], '1 2 3 4')
        self.assertEqual(print_calls[2].args[0], '1 2 3 4')
        self.assertEqual(print_calls[2].args[0], '1 2 3 4')

class TestSeries(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.side_effect = ['5', '4']
        import series
        reload(series)
        self.assertEqual(2, input_call.call_count)
        input_calls = input_call.call_args_list
        self.assertEqual(input_calls[0].args[0], 'denominator ratio (k): ')
        self.assertEqual(input_calls[1].args[0], 'number of terms (n): ')
        print_call.assert_called_once()
        print_calls = print_call.call_args_list
        print_str = print_calls[0].args[0]
        self.assertEqual('sum: 1.', print_str[:7])
        sum = float(print_str[5:])
        self.assertAlmostEqual(1.248000, sum)

class TestReading(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.side_effect = ['50', '1', '100']
        import reading
        reload(reading)
        self.assertEqual(3, input_call.call_count)
        input_calls = input_call.call_args_list
        self.assertEqual(input_calls[0].args[0], 'Pages to read? ')
        self.assertEqual(input_calls[1].args[0], 'Days left? ')
        self.assertEqual(input_calls[2].args[0], 'Pages read: ')
        self.assertEqual(3, print_call.call_count)
        print_calls = print_call.call_args_list
        self.assertEqual(print_calls[0], call())
        self.assertEqual(print_calls[1].args[0], 'You have read 100 out of 50 pages.')
        self.assertEqual(print_calls[2].args[0], '-50 pages left, 0 days to go.')
