'''2124. Check if All A's Appears Before All B's'''


class Solution:
    def checkString(self, s: str) -> bool:
        return ''.join(sorted(s)) == s


s = Solution()
print(s.checkString('aaabbb'))
