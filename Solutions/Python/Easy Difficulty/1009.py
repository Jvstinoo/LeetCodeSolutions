'''1009. Complement of Base 10 Integer'''


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin = [1]
        nn = n
        for i in range(n):
            if bin[-1]*2 <= n:
                bin.append(bin[-1]*2)
            else:
                break
        bin.reverse()
        reverse_bin = ''
        for j in bin:
            if j <= nn:
                reverse_bin += '0'
                nn -= j
            else:
                reverse_bin += '1'
        out = 0

        for index, ele in enumerate(reverse_bin):
            if ele == '1':
                out += bin[len(bin)-len(reverse_bin):][index]

        return out


s = Solution()
print(s.bitwiseComplement(10))
