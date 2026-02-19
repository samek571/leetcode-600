class Solution:
    def countLargestGroup(self, n: int) -> int:

        #i bet this could be put into one line but ffs
        hsh = defaultdict(int)
        for i in range(1, n + 1):
            hsh[sum(map(int, list(str(i))))] +=1

        return sum(1 for i in hsh.values() if i >= max(hsh.values()))
