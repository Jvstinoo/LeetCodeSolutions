'''217. Contains Duplicate'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

    '''Alt solution:
            return len(set(nums)) != len(nums)'''
