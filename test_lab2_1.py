# unitttest is a testing suite in Standard Library.
# I understand this is built to mimic JTest, but I don't know JTest.
import unittest
# Need this in order to mock built-in functions
import builtins
# patch allows me to replace functions/classes with 'mock' versions
# that we can feed test values to, inspect calls to, etc.
from unittest.mock import patch
# I only use call to check on empty calls to print statements
from unittest.mock import call

class TestDashes(unittest.TestCase):
    # This is a built-in method that unittest automatically looks for.
    @classmethod
    def setUpClass(cls):
        print("\n"*5)
    # This means I am replacing input() and print() with mock versions of these
    # for the purposes of this test.
    # The @patch decorator requires a module name, that's why we need builtins.
    @patch('builtins.input')
    @patch('builtins.print')
    # The names in the call to test_main are the mock versions of the functions
    # above, in reverse order. I'm not clear on why in reverse order, but it is.
    def test_main(self, print_call, input_call):
        # Set up the value for the input() before we call the script
        input_call.return_value = 'bishops'
        # unittest treats everything as a module.
        # unittest automatically runs the script upon import, it runs everything
        # with the intent of creating the functions and classes in memory.
        # Of course, if you have no functions or classes, it just runs it.
        import dashes
        # Check that input() was called exactly once.
        input_call.assert_called_once
        # Check that input() was fed the exactly correct argument.
        input_call.assert_called_with('Enter text: ')
        # Similar test for print().
        print_call.assert_called_once
        print_call.assert_called_with('-b-i-s-h-o-p-s-')

class TestPatterns(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.return_value = '3'
        import patterns
        input_call.assert_called_once
        input_call.assert_called_with('Enter a number to generate a cool pattern: ')
        # With more than one call, we use .call_count instead
        self.assertEqual(3, print_call.call_count)
        # We can't just use assert_called_with() because print() was called
        # more than once.
        # Each call() object has a list of args and a list of kwargs.
        print_calls = print_call.call_args_list
        # One could also test that there was exactly one argument in each
        # print() call's args, and no kwargs, but I didn't bother.
        self.assertEqual(print_calls[0].args[0], '1 2 3')
        self.assertEqual(print_calls[1].args[0], '1 2 3')
        self.assertEqual(print_calls[2].args[0], '1 2 3')

class TestSeries(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        # Side effects handle more complex situations like successive calls.
        # We have two calls to input(), so we need to feed one value for the
        # first call and another value for the second call.
        input_call.side_effect = ['2', '5']
        import series
        self.assertEqual(2, input_call.call_count)
        input_calls = input_call.call_args_list
        self.assertEqual(input_calls[0].args[0], 'denominator ratio (k): ')
        self.assertEqual(input_calls[1].args[0], 'number of terms (n): ')
        print_call.assert_called_once()
        print_calls = print_call.call_args_list
        print_str = print_calls[0].args[0]
        # This test the string part of the output
        self.assertEqual('sum: 1.', print_str[:7])
        # Now we convert the numerical part to a float and check if that is
        # close enough to the actual value.  unittest provides 'AlmostEqual'
        # to test if floats are close enough to assume they are the same.
        # Default tolerance is within 10^(-7).
        sum = float(print_str[5:])
        self.assertAlmostEqual(1.9375, sum)

class TestReading(unittest.TestCase):
    @patch('builtins.input')
    @patch('builtins.print')
    def test_main(self, print_call, input_call):
        input_call.side_effect = ['100', '5', '20', '30', '0', '0', '45']
        import reading
        self.assertEqual(7, input_call.call_count)
        input_calls = input_call.call_args_list
        self.assertEqual(input_calls[0].args[0], 'Pages to read? ')
        self.assertEqual(input_calls[1].args[0], 'Days left? ')
        self.assertEqual(input_calls[2].args[0], 'Pages read: ')
        self.assertEqual(input_calls[3].args[0], 'Pages read: ')
        self.assertEqual(input_calls[4].args[0], 'Pages read: ')
        self.assertEqual(input_calls[5].args[0], 'Pages read: ')
        self.assertEqual(input_calls[6].args[0], 'Pages read: ')
        self.assertEqual(15, print_call.call_count)
        print_calls = print_call.call_args_list
        self.assertEqual(print_calls[0], call())
        self.assertEqual(print_calls[1].args[0], 'You have read 20 out of 100 pages.')
        self.assertEqual(print_calls[2].args[0], '80 pages left, 4 days to go.')
        self.assertEqual(print_calls[3], call())
        self.assertEqual(print_calls[4].args[0], 'You have read 50 out of 100 pages.')
        self.assertEqual(print_calls[5].args[0], '50 pages left, 3 days to go.')
        self.assertEqual(print_calls[6], call())
        self.assertEqual(print_calls[7].args[0], 'You have read 50 out of 100 pages.')
        self.assertEqual(print_calls[8].args[0], '50 pages left, 2 days to go.')
        self.assertEqual(print_calls[9], call())
        self.assertEqual(print_calls[10].args[0], 'You have read 50 out of 100 pages.')
        self.assertEqual(print_calls[11].args[0], '50 pages left, 1 days to go.')
        self.assertEqual(print_calls[12], call())
        self.assertEqual(print_calls[13].args[0], 'You have read 95 out of 100 pages.')
        self.assertEqual(print_calls[14].args[0], '5 pages left, 0 days to go.')
