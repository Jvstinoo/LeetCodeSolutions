'''1221. Split a String in Balanced Strings '''


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        out = 0
        curr_str = ''

        for index, ss in enumerate(s):

            L_count = curr_str.count('L')
            R_count = curr_str.count('R')
            if (L_count == 0 or R_count == 0) or (L_count != R_count):
                curr_str += ss

            elif (L_count == R_count):
                out += 1
                curr_str = ss
        out += 1

        return out
