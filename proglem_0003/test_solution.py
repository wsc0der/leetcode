import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_solution(self):
        cases = (('abcabcbb', 3),
                 ('bbbbb', 1),
                 ('pwwkew', 3),
                 (' ', 1),
                 ('aab', 2))
        s = Solution()
        for input, result in cases:
            with self.subTest():
                self.assertEqual(s.lengthOfLongestSubstring(input), result)