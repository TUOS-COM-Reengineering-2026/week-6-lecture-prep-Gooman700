import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    def test_strange_function1(self):
        self.assertEqual(
            first=strange_function(1, 1, 3, 4),
            second='behaviour 1'
        )

    def test_strange_function2(self):
        self.assertEqual(
            first=strange_function(1, 1, 4, 3),
            second='behaviour 2'
        )

    def test_strange_function3(self):
        self.assertEqual(
            first=strange_function(1, 2, 3, 4),
            second='behaviour 3'
        )

    def test_strange_function4(self):
        self.assertEqual(
            first=strange_function(4, 3, 2, 1),
            second='behaviour 4'
        )
    
    def test_strange_function5(self):
        self.assertEqual(
            first=strange_function(4, 1, 3, 2),
            second='behaviour 5'
        )

    def test_strange_function6(self):
        self.assertEqual(
            first=strange_function(1, 2, 1, 3),
            second='behaviour 6'
        )