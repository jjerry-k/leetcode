#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
# Your runtime beats 51.67 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        answer = ''
        tmp = str(abs(x))
        if x < 0:
            answer += '-'
        for elem in reversed(tmp):
                answer += elem
        
        answer = int(answer)
        if answer > 2**31-1 or answer < -(2**31):
            answer = 0
        return answer

        
# @lc code=end