class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        q_end = [[] for _ in range(n)]
        for start, end in queries:
            q_end[start].append(end)

        pq = []
        semi_res = [0] * (n + 1)
        d = 0

        for i in range(n):
            d += semi_res[i]
            for end in q_end[i]:
                heapq.heappush(pq, -end)
            x = nums[i]


            while pq and x > d:
                if -pq[0] < i: break
                k = -heapq.heappop(pq)
                if k + 1 <= n:
                    semi_res[k+1] -= 1
                d += 1

            if x > d:
                return -1

        return len(pq)
