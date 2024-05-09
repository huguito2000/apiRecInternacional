from test.happyPath import happypath
import unittest
from unittest import TestCase

class MyTests(TestCase):
    def test_one(self):
        self.assertEqual(1, 1)
        happypath()

if __name__ == '__main__':
    unittest.main()