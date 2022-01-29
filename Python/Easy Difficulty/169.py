'''169. Majority Element'''
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''First Solution (its the same as second but Counter does the work for me)'''
        occurences = Counter(nums)
        return [k for k, v in occurences.items() if v > len(nums)/2][0]

        '''Second Solutuion'''

        occurences = {}

        for i in nums:
            occurences[i] = occurences.get(i, 0) + 1

            if occurences[i] > len(nums)/2:
                return i


s = Solution()
print(s.majorityElement([3, 2, 3]))
