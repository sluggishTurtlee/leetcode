class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)

        list_a = list(a)
        list_b = list(b)

        list_a.reverse()
        list_b.reverse()

        dec_a = 0
        dec_b = 0

        for i in range(len_a):
            dec_a += int(list_a[i]) * 2**i

        for j in range(len_b):
            dec_b += int(list_b[j]) * 2**j

        sum_ab = dec_a + dec_b
        bin_ab = str(bin(sum_ab))
        list_ab = list(bin_ab)

        list_ab.remove("0")
        list_ab.remove("b")

        return ''.join(list_ab)
