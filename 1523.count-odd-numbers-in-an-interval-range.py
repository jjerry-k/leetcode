#
# @lc app=leetcode id=1523 lang=python3
#
# [1523] Count Odd Numbers in an Interval Range
# Your runtime beats 31.76 % of python3 submissions
# Your memory usage beats 13.03 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        half_of_tot_num_cnt = (high - low + 1)//2
        low_cond = 0 if low % 2 == 0 else 1
        high_cond = 0 if high % 2 == 0 else 1
        return half_of_tot_num_cnt+1 if low_cond and high_cond else half_of_tot_num_cnt
# @lc code=end