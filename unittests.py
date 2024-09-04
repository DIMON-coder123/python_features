import unittest
import decimal

def add_two_number(a, b):
    return a + b


class TestAddTwoNumbers(unittest.TestCase):

    def test_add_two_positive(self):
        result = add_two_number(4, 5)
        self.assertEqual(result, 9)


    def test_add_two_negative(self):
        result = add_two_number(-4, -5)
        self.assertEqual(result, -9)

    def test_add_positive_negative(self):
        result = add_two_number(-4, 5)
        self.assertEqual(result, 1)


    def test_add_two_zero(self):
        result = add_two_number(0, 5)
        self.assertEqual(result, 5)


    def test_add_zero_to_zero(self):
        result = add_two_number(0, 0)
        self.assertEqual(result, 0)


    def test_add_large_numbers(self):
        result = add_two_number(999_999_999, 1)
        self.assertEqual(result, 1_000_000_000)


    def test_add_two_floats(self):
        result = add_two_number(4.2, 5.4)
        self.assertAlmostEqual(result, 9.6)


    def test_add_to_None(self):
        with self.assertEqual(TypeError):
            add_two_number(None, 2)


    def test_add_to_string(self):
        with self.assertEqual(TypeError):
            add_two_number('one', 2)





if __name__ == '__main__':
    unittest.main()