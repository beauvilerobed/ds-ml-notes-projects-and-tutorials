import unittest
from intersection_of_lists import intersection
import random


class Intersection(unittest.TestCase):
    def test_small(self):
        test_case = [
            ([], ['1', '5', '3'], []),
            (['1', '5', '3'], ['0', '5', '3'], ['5', '3']),
        ]
        for a, b, ans in test_case:
            self.assertEqual(set(intersection(a,b)), set(ans))

    def test_large(self):
        test_1_a = [random.randint(50, 100) for _ in range(10**5)]
        test_1_b = [random.randint(50, 100) for _ in range(10**5)]
        test_case = [
            (test_1_a,
             test_1_b,
             set(test_1_a).intersection(test_1_b)),
            ([1]*10**5,
             [0]*10**5,
             []),
        ]
        for a, b, ans in test_case:
            self.assertEqual(set(intersection(a,b)), set(ans))


if __name__ == '__main__':
    unittest.main()
