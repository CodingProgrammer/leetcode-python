#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if None == root:
            return 0
        d, D = sorted(map(self.minDepth,(root.left, root.right)))
        return 1 + (d or D)