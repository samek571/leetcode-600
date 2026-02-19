class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        curr_lvl, res, _max = 1, 1, float('-inf')

        q = deque([root])
        while q:

            curr_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                curr_sum += node.val

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            if curr_sum > _max:
                _max = curr_sum
                res = curr_lvl

            curr_lvl += 1

        return res
