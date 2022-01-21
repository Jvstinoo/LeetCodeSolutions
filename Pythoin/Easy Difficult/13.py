'''13. Roman to Integer'''


class Solution:
    def romanToInt(self, s: str) -> int:
        vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                'C': 100, 'D': 500, 'M': 1000}
        out = 0
        for i in range(0, len(s)-1):
            if vals[s[i]] >= vals[s[i+1]]:
                out += vals[s[i]]
            else:
                out -= vals[s[i]]
        out += vals[s[-1]]
        return out


s = Solution()
print(s.romanToInt("III"))
