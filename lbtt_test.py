import unittest
from lbtt import calculate_lbtt

class TestLBTT(unittest.TestCase):
    def test_no(self):
        self.assertEqual(calculate_lbtt(100000),0)
    def test_low(self):
        self.assertEqual(calculate_lbtt(200000),1100)
    def test_mid(self):
        self.assertEqual(calculate_lbtt(300000),4600)
    def test_high(self):
        self.assertEqual(calculate_lbtt(400000),13350)
    def test_top(self):
        self.assertEqual(calculate_lbtt(800000),54350)

if __name__ == '__main__':
    unittest.main()