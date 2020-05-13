#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
# Your runtime beats 16.6 % of python3 submissions
# Your memory usage beats 5.21 % of python3 submissions (16.8 MB)
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0 
# @lc code=end