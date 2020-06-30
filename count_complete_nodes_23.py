#Count Complete Tree Nodes

#Solution
#Given a complete binary tree, count the number of nodes.

#Note:

#Definition of a complete binary tree from Wikipedia:
#In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

#Example:

#Input: 
#    1
#   / \
#  2   3
# / \  /
#4  5 6

#Output: 6

#Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = r = 0
        left = right = root
        while left or right:
            if left:
                l += 1
                left = left.left
            if right:
                r += 1
                right = right.right
        
        if l == r:
            return 2**l - 1
        else:
            return 1 + self.countNodes(root.right) + self.countNodes(root.left)