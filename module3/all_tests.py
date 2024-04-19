import unittest
from functions import is_one_to_one, is_onto, is_bijection
from sets import intersection_of_sets, union_of_sets


class SetsTests(unittest.TestCase):

    def test_set_intersection(self):
        setA = [12, 7, 9, 8, 2]
        setB = [3, 2, 12, 9, 8]
        result = intersection_of_sets(setA, setB)
        self.assertEqual(4, len(result))
        self.assertEqual(2, result[0])
        self.assertEqual(8, result[1])
        self.assertEqual(9, result[2])
        self.assertEqual(12, result[3])

    def test_set_union(self):
        setA = [12, 7, 9, 8, 2]
        setB = [3, 2, 12, 9, 8]
        result = union_of_sets(setA, setB)
        self.assertEqual(6, len(result))
        self.assertEqual(2, result[0])
        self.assertEqual(3, result[1])
        self.assertEqual(7, result[2])
        self.assertEqual(8, result[3])
        self.assertEqual(9, result[4])
        self.assertEqual(12, result[5])


class FunctionsTests(unittest.TestCase):

    def test_function_properties_equal_same_order_both(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 2, 12, 9, 8]
        range = [3, 2, 12, 9, 8]
        self.assertTrue(is_one_to_one(domain, target, range))
        self.assertTrue(is_onto(domain, target, range))
        self.assertTrue(is_bijection(domain, target, range))

    def test_function_properties_both_different_order(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 2, 12, 9, 8]
        range = [3, 9, 12, 8, 2]
        self.assertTrue(is_one_to_one(domain, target, range))
        self.assertTrue(is_onto(domain, target, range))
        self.assertTrue(is_bijection(domain, target, range))

    def test_function_properties_onto_different_order(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 12, 9, 8]
        range = [8, 9, 12, 3, 8]
        self.assertFalse(is_one_to_one(domain, target, range))
        self.assertTrue(is_onto(domain, target, range))
        self.assertFalse(is_bijection(domain, target, range))

    def test_function_properties_not_one_to_one_same_order(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 2, 12, 9, 8, 4]
        range = [3, 2, 12, 9, 9]
        self.assertFalse(is_one_to_one(domain, target, range))
        self.assertFalse(is_onto(domain, target, range))
        self.assertFalse(is_bijection(domain, target, range))

    def test_function_properties_not_one_to_one_different_order(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 2, 12, 9, 8, 4]
        range = [8, 4, 12, 4, 3]
        self.assertFalse(is_one_to_one(domain, target, range))
        self.assertFalse(is_onto(domain, target, range))
        self.assertFalse(is_bijection(domain, target, range))

    def test_function_properties_one_to_one(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 2, 12, 9, 8, 4]
        range = [3, 2, 12, 9, 8]
        self.assertTrue(is_one_to_one(domain, target, range))
        self.assertFalse(is_onto(domain, target, range))
        self.assertFalse(is_bijection(domain, target, range))

    def test_function_properties_one_to_one_2(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 2, 12, 9, 8, 4]
        range = [8, 4, 12, 9, 3]
        self.assertTrue(is_one_to_one(domain, target, range))
        self.assertFalse(is_onto(domain, target, range))
        self.assertFalse(is_bijection(domain, target, range))

    def test_function_properties_onto(self):
        domain = [12, 7, 9, 8, 2]
        target = [3, 2, 9, 8]
        range = [3, 2, 3, 9, 8]
        self.assertFalse(is_one_to_one(domain, target, range))
        self.assertTrue(is_onto(domain, target, range))
        self.assertFalse(is_bijection(domain, target, range))


if __name__ == '__main__':
    unittest.main()

