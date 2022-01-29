'''961. N-Repeated Element in Size 2N Array'''
from typing import List
from collections import Counter


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        occurences = Counter(nums)

        return dict(zip(occurences.values(), occurences.keys()))[len(nums)//2]


s = Solution()
print(s.repeatedNTimes([1, 2, 3, 3]))
print(s.repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]))
