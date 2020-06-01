#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
# Your runtime beats 41.29 % of python3 submissions
# Your memory usage beats 11.11 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
        return " ".join([(val if val[0].lower() in 'aeiou' else val[1:]+val[0])+'m'+('a'*(i+2)) for i, val in enumerate(S.split(' '))])
# @lc code=end

