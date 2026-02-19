class Solution:
    #bruteforce i know but its easy one and i dont have time for daily challenge that much
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                if abs(arr[i] - arr[j]) > a: continue

                for k in range(j + 1, n):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res
