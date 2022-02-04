'''680. Valid Palindrome II'''


class Solution:
    def validPalindrome(self, s: str) -> bool:
        pointerL = 0
        pointerR = len(s)-1

        while pointerL < pointerR:
            if s[pointerL] != s[pointerR]:
                pL_forward = s[pointerL+1:pointerR+1]
                pR_backwards = s[pointerL:pointerR]
                return (pL_forward == pL_forward[::-1]) or (pR_backwards == pR_backwards[::-1])

            pointerL += 1
            pointerR -= 1

        return True


s = Solution()
print(s.validPalindrome('abca'))
