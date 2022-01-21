'''35. Search Insert'''
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == target:
                return i
            if nums[i] < target:
                return i+1

        return 0
