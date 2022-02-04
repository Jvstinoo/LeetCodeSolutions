'''67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''


class Solution:
    def createBinChart(self, n):
        binary = [1]
        [binary.append(binary[-1]*2) for i in range(n) if binary[-1]*2 <= n]
        return binary[::-1]

    def convertToInt(self, s):
        binChart = [1]
        [binChart.append(binChart[-1]*2) for i in range(len(s)-1)]
        binChart.reverse()
        return binChart, sum([binChart[i] for i, ele in enumerate(binChart) if s[i] == '1'])

    def main(self, binA, binB):
        total = self.convertToInt(binA)[1] + self.convertToInt(binB)[1]
        out = ''
        final_bin = self.createBinChart(total)
        for i in range(len(final_bin)):
            if final_bin[i] <= total:
                out += '1'
                total -= final_bin[i]
            else:
                out += '0'
        return out


s = Solution()
print(s.main('11', '1'))
print(s.main('1010', '1011'))
