'''1528. Shuffle String'''
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ordering = {indices[i]: s[i] for i in range(len(s))}
        return ''.join([ordering[i] for i in range(len(indices))])
