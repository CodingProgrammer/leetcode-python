# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        stack = [[root.left, root.right]]
        while len(stack) > 0:
            pair = stack.pop(0)
            left = pair[0]
            right = pair[1]
            if None == left and None == right:
                continue
            elif None == left or None == right:
                return False
            elif left.val == right.val:
                stack.insert(0,[left.left, right.right])
                stack.insert(0,[left.right, right.left])
            else:
                return False
        return True
