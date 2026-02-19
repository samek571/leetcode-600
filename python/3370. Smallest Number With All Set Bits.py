class Solution:
    def smallestNumber(self, n: int) -> int:
        return 2**int(log2(n)+1)-1 #15 == 1111 == 2^4-1
