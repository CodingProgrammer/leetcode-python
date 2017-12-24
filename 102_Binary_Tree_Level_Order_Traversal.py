# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        def preOrder(root, level):
            if None != root :
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(root.val)
                preOrder(root.left, level + 1)
                preOrder(root.right, level + 1)
        preOrder(root, 0)
        return ans