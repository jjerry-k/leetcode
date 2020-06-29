#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
# Your runtime beats 99.67 % of python3 submissions
# Your memory usage beats 5.72 % of python3 submissions (13.7 MB)
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if not p and not q:
            return True
        
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# @lc code=end

