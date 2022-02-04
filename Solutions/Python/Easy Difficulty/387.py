from typing import List
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        '''ind = {}
        for i in range(len(s)):
            ind[s[i]] = ind.get(s[i], 0) + 1

        if 1 in ind.values():
            return s.index([k for k,v in ind.items() if v == 1][0])
        return -1'''

        counter = Counter(s)
        if 1 in counter.values():
            return s.index([k for k, v in counter.items() if v == 1][0])
        return -1
