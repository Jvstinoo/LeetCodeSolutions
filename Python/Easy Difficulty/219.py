'''219. Contains Duplicate II'''
from typing import List
from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        for index, num in enumerate(nums):
            if counter[num] > 1:
                pA = index
                pB = len(nums)-1
                while pB > pA:
                    if nums[pB] == num:
                        if abs(index-pB) <= k:
                            return True
                    pB -= 1
        return False


s = Solution()
print(s.containsNearbyDuplicate([1, 0, 1, 1], 1))
