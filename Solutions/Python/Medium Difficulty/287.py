'''287. Find the Duplicate Number'''
from collections import Counter


class Solution:
    def findDuplicate(self, nums):
        ind = {}

        for j, i in enumerate(nums):
            if i not in ind:
                ind[i] = j
            else:
                return i


s = Solution()
print(s.findDuplicate([2, 2, 3]))
print(s.findDuplicate([2, 2, 2, 2, 2]))
