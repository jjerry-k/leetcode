#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
# Your runtime beats 93.93 % of python3 submissions
# Your memory usage beats 45.29 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.replace("-", "").upper()[::-1]
        return '-'.join(S[i:i+K] for i in range(0, len(S), K))[::-1]
# @lc code=end