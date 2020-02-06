#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#

# @lc code=start
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return [int(i) for i in str(int("".join([str(i) for i in A])) + K)]
# @lc code=end

