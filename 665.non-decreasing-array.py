#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
# Your runtime beats 60.07 % of python3 submissions
# Your memory usage beats 67.72 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        a = nums[:]
        b = nums[:]
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                a.pop(i)
                b.pop(i+1)
                if (sorted(a) != a) and (sorted(b)!=b):
                    return False
                    break
        return True
# @lc code=end