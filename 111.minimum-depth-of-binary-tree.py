#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
# Your runtime beats 84.02 % of python3 submissions
# Your memory usage beats 56.76 % of python3 submissions (15.4 MB)
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1
# @lc code=end

