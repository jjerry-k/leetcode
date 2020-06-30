#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
# Your runtime beats 36.87 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums_1, nums_2, result = nums[:n], nums[n:], []
        for i in range(n):
            result += [nums_1[i], nums_2[i]]
        return result
# @lc code=end

