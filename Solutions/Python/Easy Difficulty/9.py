'''9. Palindrome Number'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Bad solution :(
        # return str(x) == str(x)[::-1]
        if x < 0:
            return False

        out = []
        compare = []

        while x != 0:
            out.append(x % 10)
            compare.insert(0, x % 10)
            x //= 10

        return out == compare


s = Solution()
print(s.isPalindrome(20))
print(s.isPalindrome(121))
