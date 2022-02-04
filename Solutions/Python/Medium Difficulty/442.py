'''442. Find All Duplicates in an Array'''
from collections import Counter


class Solution:
    def findDuplicates(self, nums):
        return [k for k, v in Counter(nums).items() if v > 1]

        '''Same Solution basically'''
        counter = {}
        for i in nums:
            counter[i] = counter.get(i, 0) + 1
        return [k for k, v in counter.items() if v > 1]


s = Solution()
print(s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))
