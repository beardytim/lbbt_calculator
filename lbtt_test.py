import unittest
from lbtt import calculate_lbtt

class TestLBTT(unittest.TestCase):
    def test_no(self):
        self.assertEqual(calculate_lbtt(100000),0.0)
    def test_low(self):
        self.assertEqual(calculate_lbtt(200000),1100.0)
    def test_mid(self):
        self.assertEqual(calculate_lbtt(300000),4600.0)
    def test_high(self):
        self.assertEqual(calculate_lbtt(400000),13350.0)
    def test_top(self):
        self.assertEqual(calculate_lbtt(800000),54350.0)
    def test_edge_one(self):
        self.assertEqual(calculate_lbtt(145001),0.02)
    def test_edge_two(self):
        self.assertEqual(calculate_lbtt(249999),2099.98)
    def test_edge_three(self):
        self.assertEqual(calculate_lbtt(250000),2100.0)
    def test_edge_four(self):
        self.assertEqual(calculate_lbtt(250001),2100.05)
    def test_edge_five(self):
        self.assertEqual(calculate_lbtt(750000),48350.0)
    def test_edge_six(self):
        self.assertEqual(calculate_lbtt(2000000),198350.0)

if __name__ == '__main__':
    unittest.main()