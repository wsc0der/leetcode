from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i in range(len(nums)):
            n = nums[i]
            m = target - n
            if m in index_map:
                return [i, index_map[m]]
            index_map[n] = i
