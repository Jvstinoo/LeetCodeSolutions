'''2073. Time Needed to Buy Tickets'''
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ticks = tickets[:]
        out = 0
        while ticks[k] != 0:
            for index, person in enumerate(ticks):
                if person > 0:
                    ticks[index] -= 1
                    out += 1
                if ticks[k] == 0:
                    break

        return out
