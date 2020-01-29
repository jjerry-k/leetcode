#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        n_b, n_a, n_l, n_o, n_n= text.count('b'), text.count('a'), text.count('l')//2, text.count('o')//2, text.count('n')
        return min([n_b, n_a, n_l, n_o, n_n])

# @lc code=end

