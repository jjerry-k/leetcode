#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
# Your runtime beats 39.69 % of python3 submissions
# Your memory usage beats 55 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return [int(i) for i in str(int("".join([str(i) for i in A])) + K)]
# @lc code=end

