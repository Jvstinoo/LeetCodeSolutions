'''989. Add to Array-Form of Integer'''
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        out = int(''.join([str(i) for i in num])) + k

        return [int(i) for i in str(out)]
