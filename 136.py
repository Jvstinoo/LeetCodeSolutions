'''136. Single Number'''
from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #counter = Counter(nums)
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        return [k for k, v in counter.items() if v == 1][0]


s = Solution()

print(s.singleNumber([4, 1, 2, 1, 2]))

# 1, 1, 2, 2, 4 returns 4
