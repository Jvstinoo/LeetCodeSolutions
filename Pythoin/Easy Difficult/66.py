'''66. Plus One'''
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        '''Other solution:
        out = str(int(''.join([str(i) for i in digits]))+1)

        return [int(i) for i in out]
        '''

        return [int(i) for i in str(int(''.join([str(i) for i in digits]))+1)]


s = Solution()
print(s.plusOne([1, 2, 3]))
