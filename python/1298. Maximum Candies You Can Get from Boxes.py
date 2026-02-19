class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        dq = deque()

        for box_ind in initialBoxes:
            for key in keys[box_ind]:
                status[key] = 1

            if status[box_ind] == 0:
                dq.append(box_ind)
            else:
                dq.appendleft(box_ind)


        res = 0
        while dq:
            ind = dq.popleft()

            if status[ind] == 0:
                break
            elif status[ind] == 1:
                res += candies[ind]
                for key in keys[ind]:
                    status[key] = 1

            for new_box_ind in containedBoxes[ind]:
                if status[new_box_ind] == 0:
                    dq.append(new_box_ind)
                else:
                    dq.appendleft(new_box_ind)

        return res
