import unittest
import builtins
from unittest.mock import patch, call
from importlib import reload

class TestPatterns(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.return_value = '5'
        import patterns
        reload(patterns)
        input_call.assert_called_once
        input_call.assert_called_with('Enter a number to generate a cool pattern: ')
        self.assertEqual(5, print_call.call_count)
        print_calls = print_call.call_args_list
        self.assertEqual(print_calls[0].args[0], '1 2 3 4 5')
        self.assertEqual(print_calls[1].args[0], '1 2 3 4 5')
        self.assertEqual(print_calls[2].args[0], '1 2 3 4 5')
        self.assertEqual(print_calls[2].args[0], '1 2 3 4 5')
        self.assertEqual(print_calls[2].args[0], '1 2 3 4 5')

class TestSeries(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.side_effect = ['3', '7']
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
        self.assertAlmostEqual(1.4993141, sum)
