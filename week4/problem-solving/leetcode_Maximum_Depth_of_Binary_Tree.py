# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorder(root, count=0):
    if root == None:
        return count
    
    count = count+1
    count_left = preorder(root.left, count)
    count_right = preorder(root.right, count)
    
    return max(count_left, count_right)

class Solution:
    def maxDepth(self, root):
        count = 0
        count = preorder(root)

        return count
    
