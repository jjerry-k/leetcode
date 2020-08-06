#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
# Your runtime beats 5.79 % of python3 submissions
# Your memory usage beats 6.59 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [x for x in range(left, right+1) if all([int(i) != 0 and x % int(i)==0 for i in str(x)])]
# @lc code=end