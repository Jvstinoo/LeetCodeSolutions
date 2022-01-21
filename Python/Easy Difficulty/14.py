'''14. Longest Common Prefix'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        out = ''

        for index, j in enumerate(min(strs)):
            if len(set([i[index] for i in strs])) == 1:
                out += j
            else:
                return out
        return out


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
