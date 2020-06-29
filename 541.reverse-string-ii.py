#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
# Your runtime beats 61.43 % of python3 submissions
# Your memory usage beats 14.29 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        tmp = list(s)
        for i in range(0, len(tmp), k*2):
            tmp[i:i+k] = tmp[i:i+k][::-1]
        return "".join(tmp)
# @lc code=end

