'''1920. Build Array from Permutation'''
from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        '''out = []
        for i in range(len(nums)):
            out.append(nums[nums[i]])

        return out'''

        return [nums[nums[i]] for i in range(len(nums))]
