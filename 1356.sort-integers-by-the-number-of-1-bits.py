#
# @lc app=leetcode id=1356 lang=python3
#
# [1356] Sort Integers by The Number of 1 Bits
# Your runtime beats 91.92 % of python3 submissions
# Your memory usage beats 20.79 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: [bin(x).count("1"), x])
        # return sorted(sorted(arr), key=lambda x: bin(x)[2:].count("1"))
# @lc code=end