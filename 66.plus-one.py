#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
# Your runtime beats 50.8 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(i) for i in str(int("".join([str(i) for i in digits]))+1)]
# @lc code=end

