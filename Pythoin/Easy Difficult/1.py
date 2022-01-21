'''1. Two Sum'''
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''indices = {}
        for j, i in enumerate(nums):
            if target-i in indices:
                return [j, indices[target-i]]
            indices[i] = j'''

        for index, num in enumerate(nums):
            needed_num = target-num
            if needed_num in nums[index+1:]:
                return [index, nums[index+1:].index(needed_num)+1+index]


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([3, 3], 6))
print(s.twoSum([3, 2, 4], 6))
