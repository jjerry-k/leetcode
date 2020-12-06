#
# @lc app=leetcode id=942 lang=python3
#
# [942] DI String Match
# Your runtime beats 93.26 % of python3 submissions
# Your memory usage beats 8.54 % of python3 submissions (15.3 MB)
# @lc code=start
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        left = right = 0
        output = [0]
        for i in S:
            if i == "I":
                right += 1
                output.append(right)
            else:
                left -= 1
                output.append(left)
        return [i - left for i in output]
# @lc code=end