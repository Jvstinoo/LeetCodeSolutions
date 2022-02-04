'''2057. Smallest Index With Equal Value'''
from typing import List


class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        try:
            return min([i for i in range(len(nums)) if i % 10 == nums[i]])
        except:
            return -1

        '''for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
            
        return -1'''
