# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, l=None, r=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node, d):
            if not node:
                return (None, d)

            l_lca, l_d = dfs(node.left, d + 1)
            r_lca, r_d = dfs(node.right, d + 1)

            if l_d > r_d:
                return (l_lca, l_d)
            elif r_d > l_d:
                return (r_lca, r_d)
            else:
                return (node, l_d)

        res, _ = dfs(root, 0)
        return res
