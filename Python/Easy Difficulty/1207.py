'''1207. Unique Number of Occurrences'''
from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = Counter(arr).values()
        return len(set(occurences)) == len(occurences)
        '''occurences = {}
        
        for i in arr:
            occurences[i] = occurences.get(i, 0) + 1
            
        return len(occurences.values()) == len(set(occurences.values()))'''
