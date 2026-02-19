# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        def inorder_dfs(node):
            if not node: return []
            return inorder_dfs(node.left) + [node.val] + inorder_dfs(node.right)

        vert = inorder_dfs(root)
        def do_(l, r):
            if l > r: return None
            mid = (l + r) // 2
            root = TreeNode(vert[mid])
            root.left, root.right = do_(l, mid-1), do_(mid + 1, r)
            return root

        return do_(0, len(vert) - 1)
