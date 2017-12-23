# Definition for a binary tree node.
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
        if None == root.left:
            return self.minDepth(root.right) + 1
        if None == root.right:
            return self.minDepth(root.left) + 1
        else:
            return 1 + min(map(self.minDepth, (root.left, root.right))) 

'''
if root is Null, return 0
if the left node is Null, return min_depth of the right node and add 1
if the right node is Null, return min_depth of the left node and add 1
otherwise, return the min_depth between left_node and right_node and add 1 
'''