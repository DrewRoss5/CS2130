import unittest
from nqueens import Nqueens
from fib import recursive_fib, fast_fib;

class NqueensTest(unittest.TestCase):

    def test_isValidFalse(self):
        q = Nqueens(2)
        q.queens = [0, 0]
        self.assertFalse(q.is_valid(2))
        q = Nqueens(2)
        q.queens = [0, 1]
        self.assertFalse(q.is_valid(2))
        q = Nqueens(3)
        q.queens = [1, 2, 0]
        self.assertFalse(q.is_valid(3))
        q = Nqueens(3)
        q.queens = [1, 2, 0]
        self.assertFalse(q.is_valid(3))
        q = Nqueens(3)
        q.queens = [1, 2, 0]
        self.assertFalse(q.is_valid(3))
        q = Nqueens(4)
        q.queens = [0, 1, 2, 3]
        self.assertFalse(q.is_valid(4))
        q = Nqueens(4)
        q.queens = [0, 2, 0, 2]
        self.assertFalse(q.is_valid(4))
        q = Nqueens(5)
        q.queens = [3, 1, 4, 2, 4]
        self.assertFalse(q.is_valid(5))
        q = Nqueens(7)
        q.queens = [0, 2, 4, 1, 3, 5, 6]
        self.assertFalse(q.is_valid(7))
        q = Nqueens(8)
        q.queens = [1, 3, 5, 7, 0, 2, 4, 6]
        self.assertFalse(q.is_valid(8))

    def test_isValidTrue(self):
        q = Nqueens(1)
        q.queens = [0]
        self.assertTrue(q.is_valid(1))
        q = Nqueens(4)
        q.queens = [1, 3, 0, 2]
        self.assertTrue(q.is_valid(4))
        q.queens = [2, 0, 3, 1]
        self.assertTrue(q.is_valid(4))
        q = Nqueens(5)
        q.queens = [3, 1, 4, 2, 0]
        self.assertTrue(q.is_valid(5))
        q.queens = [1, 3, 0, 2, 4]
        self.assertTrue(q.is_valid(5))
        q.queens = [0, 2, 4, 1, 3]
        self.assertTrue(q.is_valid(5))
        q = Nqueens(7)
        q.queens = [0, 2, 4, 6, 1, 3, 5]
        self.assertTrue(q.is_valid(7))
        q = Nqueens(8)
        q.queens = [2, 5, 7, 0, 3, 6, 4, 1]
        self.assertTrue(q.is_valid(8))

    def test_partialIsValidFalse(self):
        q = Nqueens(3)
        q.queens = [0, 0, 2]
        self.assertFalse(q.is_valid(2))
        q = Nqueens(3)
        q.queens = [0, 1, 2]
        self.assertFalse(q.is_valid(2))
        q = Nqueens(5)
        q.queens = [0, 2, 4, 3, 1]
        self.assertFalse(q.is_valid(4))
        q = Nqueens(6)
        q.queens = [1, 2, 0]
        self.assertEqual(True, q.is_valid(1))
        q = Nqueens(8)
        q.queens = [1, 2, 0]
        self.assertEqual(True, q.is_valid(1))

    def test_partialIsValidTrue(self):
        q = Nqueens(2)
        q.queens = [0, 1]
        self.assertTrue(q.is_valid(1))
        q = Nqueens(3)
        q.queens = [0, 2, 2]
        self.assertTrue(q.is_valid(2))
        q = Nqueens(5)
        q.queens = [0, 2, 4, 3, 1]
        self.assertTrue(q.is_valid(3))
        q = Nqueens(6)
        q.queens = [0, 2, 4, 1, 3, 5]
        self.assertTrue(q.is_valid(5))

class FibTest(unittest.TestCase):

    def test_recurseFib(self):
        self.assertEqual(0, recursive_fib(0))
        self.assertEqual(1, recursive_fib(1))
        self.assertEqual(1, recursive_fib(2))
        self.assertEqual(2, recursive_fib(3))
        self.assertEqual(3, recursive_fib(4))
        self.assertEqual(5, recursive_fib(5))
        self.assertEqual(21, recursive_fib(8))
        self.assertEqual(55, recursive_fib(10))
        self.assertEqual(6765, recursive_fib(20))
        self.assertEqual(832040, recursive_fib(30))
        self.assertEqual(14930352, recursive_fib(36))

    def test_fastFib(self):
        self.assertEqual(0, fast_fib(0))
        self.assertEqual(1, fast_fib(1))
        self.assertEqual(1, fast_fib(2))
        self.assertEqual(2, fast_fib(3))
        self.assertEqual(3, fast_fib(4))
        self.assertEqual(5, fast_fib(5))
        self.assertEqual(21, fast_fib(8))
        self.assertEqual(55, fast_fib(10))
        self.assertEqual(6765, fast_fib(20))
        self.assertEqual(832040, fast_fib(30))
        self.assertEqual(14930352, fast_fib(36))
        self.assertEqual(4807526976, fast_fib(48))
        self.assertEqual(10610209857723, fast_fib(64))