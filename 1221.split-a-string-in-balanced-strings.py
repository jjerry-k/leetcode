#
# @lc app=leetcode id=1221 lang=python3
#
# [1221] Split a String in Balanced Strings
# Your runtime beats 90.1 % of python3 submissions
# Your memory usage beats 90.08 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt, cond, Dict = 0, 0, {"R":1, "L":-1}
        for sub in s: 
            cond += Dict[sub]
            if cond == 0: cnt += 1
        return cnt
# @lc code=end