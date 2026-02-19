class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        hp = [(-((p + 1) / (t + 1) - p / t), p, t) for p, t in classes]
        heapq.heapify(hp)

        for _ in range(extraStudents):
            g, p, t = heapq.heappop(hp)
            p+=1; t+=1
            heapq.heappush(hp, (-((p + 1) / (t + 1) - p / t), p, t))

        return sum(p / t for _, p, t in hp) / len(classes)
