class Solution:
    def check(self, k, _tasks, _workers, _druges_left, _strength):
        lst = sorted(_workers[-k:]) # weakest k

        for task in _tasks[:k][::-1]: # hardest k tasks
            idx = bisect.bisect_left(lst, task)
            # good enough
            if idx < len(lst):
                lst.pop(idx)
            # steroids maybe?
            else:
                idx = bisect.bisect_left(lst, task - _strength)
                if idx < len(lst) and _druges_left > 0:
                    lst.pop(idx)
                    _druges_left -= 1
                else:
                    return False
        return True
    ##preserves greedy as we are steroiding only the weakest, keeping the problem nondecreasing



    def maxTaskAssign(self, tasks, workers, pills, strength):
        tasks.sort()
        workers.sort()

        l, r, res = 0, min(len(tasks), len(workers)), 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.check(mid, tasks, workers, pills, strength):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
