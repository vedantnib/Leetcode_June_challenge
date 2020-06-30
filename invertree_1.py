#Invert a binary tree.

#Example:

#Input:

#     4
#   /   \
#  2     7
# / \   / \
#1   3 6   9
#Output:

#     4
#   /   \
#  7     2
# / \   / \
#9   6 3   1


#solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return
        q=[]
        q.append(root)
        while(len(q)):
            current=q[0]
            q.pop(0)
            current.left,current.right=current.right,current.left
            if (current.left):
                q.append(current.left)
            if (current.right):
                q.append(current.right)
        return root