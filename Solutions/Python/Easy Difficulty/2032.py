'''2032. Two Out of Three'''
from typing import List


class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        '''out = list(set(nums1)) + list(set(nums2)) + list(set(nums3))

        return list(set([ i for i in out if out.count(i) > 1]))'''

        a, b, c = set(nums1), set(nums2), set(nums3)
        return list((a & b) | (b & c) | (c & a))
