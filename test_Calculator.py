import unittest
from Calculator import CustomStatistics as cs
import numpy as np

class TestCustomStatistics(unittest.TestCase):

    def setUp(self):
        self.test_arr_1 = np.array([10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0])
        self.test_arr_2 = np.array([10.5, 11.5, 12.0, 13.0, 13.5, 15.0, 14.0])
        self.test_list_1 = [[1, 2], [3, 6]]
        self.test_list_2 = [[0, 1], [1, 5]]
        self.test_zero_arr = np.array([0,0])
    
    def test_p_corr(self):
        # Check wrong inputs
        self.assertRaises(TypeError, cs.p_corr, self.test_arr_1, self.test_list_1)
        self.assertRaises(TypeError, cs.p_corr, self.test_list_1, self.test_arr_1)
        self.assertRaises(ValueError, cs.p_corr, self.test_arr_1, self.test_zero_arr)

        # Check values
        self.assertIsInstance(cs.p_corr(self.test_arr_1, self.test_arr_2), float)
        self.assertAlmostEqual(cs.p_corr(self.test_arr_1, self.test_arr_2), 0.9452853)
        self.assertAlmostEqual(cs.p_corr(self.test_arr_2, self.test_arr_1), 0.9452853)

    def test_count_overlaps(self):
        # Check wrong inputs
        self.assertRaises(TypeError, cs.count_overlaps, self.test_list_1, self.test_arr_1)
        self.assertRaises(TypeError, cs.count_overlaps, self.test_arr_1, self.test_list_1)

        # Check values
        self.assertIsInstance(cs.count_overlaps(self.test_list_1, self.test_list_2), int)
        self.assertEqual(cs.count_overlaps(self.test_list_1, self.test_list_2), 3)
        self.assertEqual(cs.count_overlaps(self.test_list_2, self.test_list_1), 3)

    def test_count_overlaps_2(self):
        # Check wrong inputs
        self.assertRaises(TypeError, cs.count_overlaps_2, self.test_list_1, self.test_arr_1)
        self.assertRaises(TypeError, cs.count_overlaps_2, self.test_arr_1, self.test_list_1)

        # Check values
        self.assertIsInstance(cs.count_overlaps_2(self.test_list_1, self.test_list_2), int)
        self.assertEqual(cs.count_overlaps_2(self.test_list_1, self.test_list_2), 3)
        self.assertEqual(cs.count_overlaps_2(self.test_list_2, self.test_list_1), 3)

    def test_average(self):
        # Check wrong inputs
        self.assertRaises(TypeError, cs.average, self.test_list_1, self.test_list_2)
        self.assertRaises(TypeError, cs.average, self.test_arr_1, self.test_arr_2)
        self.assertRaises(TypeError, cs.average, self.test_arr_1, self.test_list_2)
        
        # Check value
        self.assertIsInstance(cs.average(self.test_list_1, self.test_arr_1), float)
        self.assertAlmostEqual(cs.average(self.test_list_1, self.test_arr_2), 13.25)
