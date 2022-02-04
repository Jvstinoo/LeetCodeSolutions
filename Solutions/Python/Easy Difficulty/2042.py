'''2042. Check if Numbers Are Ascending in a Sentence'''


class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = [int(i) for i in s.split() if i.isdigit()]
        return sorted(set(nums)) == nums
