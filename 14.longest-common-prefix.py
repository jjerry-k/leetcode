#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
# Your runtime beats 88.08 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        answer = ""
        words_iter = zip(*strs)
        for alpha in words_iter:
            if len(set(alpha))>1: break
            answer += alpha[0]
        return answer
# @lc code=end