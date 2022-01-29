'''728. Self Describing Numbers'''
from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        pp = [i for i in range(
            left, right+1) if all([int(j) != 0 and i % int(j) == 0 for j in str(i)])]

        return pp


s = Solution()

print(s.selfDividingNumbers(1, 22))
