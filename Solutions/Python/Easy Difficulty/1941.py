'''1941. Check if All Characters Have Equal Number of Occurrences'''


class Solution:

    def areOccurrencesEqual(self, s: str) -> bool:
        '''return len(set(Counter(s).values())) == 1'''
        out = {}
        for i in s:
            out[i] = out.get(i, 0) + 1

        return len(set(out.values())) == 1
