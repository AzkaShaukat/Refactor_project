import unittest
import os
from app.compute_statistics import ComputeStatistics


class TestComputeStatistics(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_numbers.txt"
        with open(self.test_file, "w") as f:
            f.write("10\n20\n30\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_count(self):
        stats = ComputeStatistics(self.test_file)
        self.assertEqual(stats.count_numbers(), 3)

    def test_summation(self):
        stats = ComputeStatistics(self.test_file)
        self.assertEqual(stats.summation(), 60)

    def test_average(self):
        stats = ComputeStatistics(self.test_file)
        self.assertEqual(stats.average(), 20)

    def test_minimum(self):
        stats = ComputeStatistics(self.test_file)
        self.assertEqual(stats.minimum_number(), 10)

    def test_maximum(self):
        stats = ComputeStatistics(self.test_file)
        self.assertEqual(stats.maximum_number(), 30)

    def test_empty_file(self):
        with open(self.test_file, "w") as f:
            f.write("")
        stats = ComputeStatistics(self.test_file)
        self.assertEqual(stats.count_numbers(), 0)
        self.assertEqual(stats.summation(), 0)
        self.assertEqual(stats.average(), 0)
        self.assertIsNone(stats.minimum_number())
        self.assertIsNone(stats.maximum_number())


if __name__ == '__main__':
    unittest.main()
