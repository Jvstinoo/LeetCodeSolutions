'''20. Valid Parenthesis'''


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        ss = s[:]
        while len(ss) != 0:
            if '{}' in ss:
                ss = ss.replace('{}', '')
            elif '[]' in ss:
                ss = ss.replace('[]', '')
            elif '()' in ss:
                ss = ss.replace('()', '')
            else:
                if len(ss) > 1:
                    return False

        return True
