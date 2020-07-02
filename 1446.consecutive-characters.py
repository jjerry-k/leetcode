#
# @lc app=leetcode id=1446 lang=python3
#
# [1446] Consecutive Characters
# Your runtime beats 86.74 % of python3 submissions
# Your memory usage beats 64.88 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def maxPower(self, s: str) -> int:
        max_cnt = 1
        tmp_cnt = 1
        prev_elem = s[0]
        for elem in s[1:]:
            if prev_elem == elem: tmp_cnt += 1
            else:
                tmp_cnt = 1
            max_cnt = tmp_cnt if tmp_cnt > max_cnt else max_cnt
            prev_elem = elem
        return max_cnt


# @lc code=end