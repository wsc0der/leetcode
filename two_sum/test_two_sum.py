import unittest
from two_sum import Solution

class TestSolution(unittest.TestCase):
    def test_two_sum(self):
        instance = Solution()
        cases = (([2,7,11,15], 9, [0,1]),
                 ([3,2,4], 6, [1,2]),
                 ([3,3], 6, [0,1]))

        for nums, target, answer in cases:
            with self.subTest():
                a = sorted(instance.twoSum(nums, target))
                b = sorted(answer)
                self.assertEqual(a, b)
