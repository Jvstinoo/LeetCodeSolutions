'''2114. Maximum Number of Words Found in Sentences'''
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        '''General Idea of solution'''
        maxx = 0
        for i in sentences:
            length = len(i.split())
            if length > maxx:
                maxx = length
        return maxx

        '''Same solution but in one line'''
        return max(len(i.split()) for i in sentences)
