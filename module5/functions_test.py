import unittest
from functions import *


class SequenceTest(unittest.TestCase):
    def test_geometric(self):
        sequence = geometric_sequence(5, 5, 2)
        self.assertEqual(5, sequence[0])
        self.assertEqual(10, sequence[1])
        self.assertEqual(20, sequence[2])
        self.assertEqual(40, sequence[3])
        self.assertEqual(80, sequence[4])
        self.assertEqual(5, len(sequence))

    def test_geometric_with_digits(self):
        sequence = geometric_sequence(7, 5.7, 2.9)
        self.assertEqual(5.7, sequence[0])
        self.assertEqual(16.53, sequence[1])
        self.assertEqual(47.94, sequence[2])
        self.assertEqual(139.02, sequence[3])
        self.assertEqual(403.15, sequence[4])
        self.assertEqual(1169.14, sequence[5])
        self.assertEqual(3390.49, sequence[6])
        self.assertEqual(7, len(sequence))

    def test_arithmetic(self):
        sequence = arithmetic_sequence(5, 5, 2)
        self.assertEqual(5, sequence[0])
        self.assertEqual(7, sequence[1])
        self.assertEqual(9, sequence[2])
        self.assertEqual(11, sequence[3])
        self.assertEqual(13, sequence[4])
        self.assertEqual(5, len(sequence))

    def test_arithmetic_with_digits(self):
        sequence = arithmetic_sequence(7, 5.73, 2.913)
        self.assertEqual(5.73, sequence[0])
        self.assertEqual(8.64, sequence[1])
        self.assertEqual(11.56, sequence[2])
        self.assertEqual(14.47, sequence[3])
        self.assertEqual(17.38, sequence[4])
        self.assertEqual(20.3, sequence[5])
        self.assertEqual(23.21, sequence[6])
        self.assertEqual(7, len(sequence))


class IntegerTest(unittest.TestCase):
    def test_div_mod_positive(self):
        self.assertEqual((3,5), div_mod(23,6))
        self.assertEqual((3,42), div_mod(246,68))
        self.assertEqual((80,2343), div_mod(259783,3218))
        self.assertEqual((7,0), div_mod(42,6))

    def test_div_mod_negative(self):
        self.assertEqual((-4,1), div_mod(-23,6))
        self.assertEqual((-4,26), div_mod(-246,68))
        self.assertEqual((-81,875), div_mod(-259783,3218))
        self.assertEqual((-7,0), div_mod(-42,6))

    def test_gcd(self):
        self.assertEqual(162, gcd(486, 324))
        self.assertEqual(12, gcd(324, 372))
        self.assertEqual(31, gcd(217, 372))
        self.assertEqual(31, gcd(372, 217))
        self.assertEqual(2, gcd(816, 422))
        self.assertEqual(5, gcd(935, 450))

    def test_lcm(self):
        self.assertEqual(972, lcm(324, 486), 972)
        self.assertEqual(10044, lcm(324, 372))
        self.assertEqual(2604, lcm(217, 372))
        self.assertEqual(172176, lcm(816, 422))
        self.assertEqual(84150, lcm(935, 450))



if __name__ == '__main__':
    unittest.main()
