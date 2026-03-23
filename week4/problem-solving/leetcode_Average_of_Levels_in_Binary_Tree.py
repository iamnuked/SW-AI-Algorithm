# https://leetcode.com/problems/average-of-levels-in-binary-tree/?envType=study-plan-v2&envId=top-interview-150

# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        avg_list = []
        while q:
            sum = 0
            q_size = len(q)
            for _ in range(q_size):
                node = q.popleft()
                sum += node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            avg_list.append(sum / q_size)
        return avg_list



