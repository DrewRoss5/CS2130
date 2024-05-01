import unittest

from matrix_relation import MatrixRelation


class Matrix_Relation_Test(unittest.TestCase):
    def setUp(self):
        self.emptyM = MatrixRelation([
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.emptyL = MatrixRelation([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        self.m1 = MatrixRelation([
            [1, 1, 0, 0, 0],
            [1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]
        ])
        self.m2 = MatrixRelation([
            [0, 1, 0, 0, 1],
            [1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1],
            [1, 0, 0, 1, 0]
        ])
        self.m3 = MatrixRelation([
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1]
        ])
        self.m4 = MatrixRelation([
            [0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        self.l1 = MatrixRelation([
            [1, 1, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 1, 0, 1]
        ])
        self.l2 = MatrixRelation([
            [0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0]
        ])
        self.l3 = MatrixRelation([
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0]
        ])



    def test_join(self):
        result = self.m1.join(self.emptyM)
        self.assertTrue(result == self.m1)
        result = self.emptyM.join(self.m1)
        self.assertTrue(result == self.m1)
        result = self.m4.join(self.m3)
        self.assertTrue(result == MatrixRelation([[1, 1, 1, 1, 1],
                                                  [0, 1, 1, 1, 1],
                                                  [1, 0, 1, 1, 1],
                                                  [0, 0, 1, 1, 1],
                                                  [0, 0, 0, 0, 1]]))

        result = self.l1.join(self.emptyL)
        self.assertTrue(result == self.l1)
        result = self.l2.join(self.l3)
        self.assertTrue(result == MatrixRelation([[0, 1, 0, 0, 1, 0, 0],
                                                  [1, 0, 0, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 0, 1, 0],
                                                  [1, 1, 1, 0, 0, 0, 0],
                                                  [1, 1, 1, 1, 0, 0, 0],
                                                  [1, 1, 1, 1, 1, 0, 1],
                                                  [1, 1, 1, 1, 1, 1, 0]]))

    def test_transpose(self):
        result = self.m2.transpose()
        self.assertTrue(self.m2 == self.m2)
        result = self.m3.transpose()
        self.assertTrue(result == MatrixRelation([[1, 0, 0, 0, 0],
                                                  [1, 1, 0, 0, 0],
                                                  [1, 1, 1, 0, 0],
                                                  [1, 1, 1, 1, 0],
                                                  [1, 1, 1, 1, 1]]))
        result = self.m4.transpose()
        self.assertTrue(result == MatrixRelation([[0, 0, 1, 0, 0],
                                                  [0, 1, 0, 0, 0],
                                                  [0, 0, 0, 1, 0],
                                                  [0, 0, 0, 0, 0],
                                                  [0, 0, 1, 0, 0]]))

        result = self.l1.transpose()
        self.assertTrue(result == MatrixRelation([[1, 1, 0, 1, 0, 0, 1],
                                                  [1, 0, 0, 0, 0, 0, 1],
                                                  [0, 1, 0, 0, 1, 0, 0],
                                                  [0, 0, 1, 0, 0, 0, 0],
                                                  [1, 0, 0, 0, 1, 0, 1],
                                                  [0, 0, 1, 1, 1, 1, 0],
                                                  [1, 0, 1, 0, 0, 1, 1]]))
        result = self.l3.transpose()
        self.assertTrue(result == MatrixRelation([[0, 1, 1, 1, 1, 1, 1],
                                                      [0, 0, 1, 1, 1, 1, 1],
                                                      [0, 0, 0, 1, 1, 1, 1],
                                                      [0, 0, 0, 0, 1, 1, 1],
                                                      [0, 0, 0, 0, 0, 1, 1],
                                                      [0, 0, 0, 0, 0, 0, 1],
                                                      [0, 0, 0, 0, 0, 0, 0]]))

    def test_reflexive_closure(self):
        result = self.m1.reflexive_closure()
        self.assertTrue(result == MatrixRelation([
                [1, 1, 0, 0, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 1, 0, 1]
        ]))
        result = self.m2.reflexive_closure()
        self.assertTrue(result == MatrixRelation([
                [1, 1, 0, 0, 1],
                [1, 1, 1, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 1, 1, 1],
                [1, 0, 0, 1, 1]
        ]))
        result = self.m3.reflexive_closure()
        self.assertTrue(result == self.m3)
        result = self.l1.reflexive_closure()
        self.assertTrue(result == MatrixRelation([
                [1, 1, 0, 0, 1, 0, 1],
                [1, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 1, 1],
                [1, 0, 0, 1, 0, 1, 0],
                [0, 0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 1, 1],
                [1, 1, 0, 0, 1, 0, 1]
        ]))
    
    def test_symmetric_closure(self):
        result = self.m1.symmetric_closure()
        self.assertTrue(result == MatrixRelation([
                [1, 1, 0, 1, 1],
                [1, 0, 1, 0, 0],
                [0, 1, 1, 0, 1],
                [1, 0, 0, 0, 0],
                [1, 0, 1, 0, 1]
        ]))
        result = self.m2.symmetric_closure()
        self.assertTrue(result == self.m2)
        result = self.m3.symmetric_closure()
        self.assertTrue(result == MatrixRelation([
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1]
        ]))
        result = self.l2.symmetric_closure()
        self.assertTrue(result == MatrixRelation([
                [0, 1, 1, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 0]
        ]))
        result = self.l3.symmetric_closure()
        self.assertTrue(result == MatrixRelation([
                [0, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1, 1, 1],
                [1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 0]
        ]))
    
    def test_in_degree(self):
        self.assertEqual(2, self.m2.in_degree(0))
        self.assertEqual(2, self.m2.in_degree(4))
        self.assertEqual(1, self.m3.in_degree(0))
        self.assertEqual(3, self.m3.in_degree(2))
        self.assertEqual(5, self.m3.in_degree(4))
        self.assertEqual(1, self.l2.in_degree(1))
        self.assertEqual(0, self.l2.in_degree(3))

    def test_out_degree(self):
        self.assertEqual(3, self.m1.out_degree(4))
        self.assertEqual(1, self.m1.out_degree(2))
        self.assertEqual(1, self.m1.out_degree(3))
        self.assertEqual(0, self.l2.out_degree(3))
        self.assertEqual(0, self.l3.out_degree(0))
        self.assertEqual(2, self.l3.out_degree(2))
        self.assertEqual(6, self.l3.out_degree(6))
    
    def test_is_rooted_tree_true(self):
        self.assertTrue(self.m4.is_rooted_tree())
        self.assertTrue(self.l2.is_rooted_tree())
    
    def test_is_rooted_tree_false(self):
        self.assertFalse(self.m1.is_rooted_tree())
        self.assertFalse(self.m2.is_rooted_tree())
        self.assertFalse(self.m3.is_rooted_tree())
        self.assertFalse(self.l1.is_rooted_tree())
        self.assertFalse(self.l3.is_rooted_tree())
    

