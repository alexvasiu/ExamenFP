import unittest
from Utils import Sort


class testSort(unittest.TestCase):
    def test_QuickSort_simple(self):
        l = [2, 8, -8, 10, 25, 1, 0, 0, 2]
        l1 = Sort.QuickSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)
        l = []
        l1 = Sort.QuickSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)
        l = [25]
        l1 = Sort.QuickSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)
        l = [2, 8, -8, 10, 25, 1, 0, 0, 2, 56, 32321321321321312, 333333333333333333333333333333333333333, 333]
        l1 = Sort.QuickSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)

    def test_QuickSort_parameters(self):
        l = [2, 8, -8, 10, 25, 1, 0, 0, 2]
        l1 = Sort.QuickSort(l, reversed=True)
        l2 = list(reversed(sorted(l)))
        self.assertEqual(l1, l2)
        l1 = Sort.QuickSort(l, key=lambda x: x * x)
        l2 = sorted(l, key=lambda x: x * x)
        self.assertEqual(l1, l2)

    def test_GnomeSort_simple(self):
        l = [2, 8, -8, 10, 25, 1, 0, 0, 2]
        l1 = Sort.GnomeSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)
        l = []
        l1 = Sort.GnomeSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)
        l = [15]
        l1 = Sort.GnomeSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)
        l = [2, 8, -8, 10, 25, 1, 0, 0, 2, 56, 32321321321321312, -2, 333]
        l1 = Sort.GnomeSort(l)
        l2 = sorted(l)
        self.assertEqual(l1, l2)

    def test_GnomeSort_parameters(self):
        l = [2, 8, -8, 10, 25, 1, 0, 0, 2]
        l1 = Sort.GnomeSort(l, reversed=True)
        l2 = list(reversed(sorted(l)))
        self.assertEqual(l1, l2)
        l1 = Sort.GnomeSort(l, key=lambda x: x * x)
        l2 = sorted(l, key=lambda x: x * x)
        self.assertEqual(l1, l2)

if __name__ == '__main__':
    unittest.main()
