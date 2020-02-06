#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
# Your runtime beats 90.96 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.2 MB)
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i for i in s.split(' ') if len(i)!=0][::-1])        
# @lc code=end