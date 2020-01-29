#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr_length = len(nums)
        return max(sum(nums[j:j+i]) for i in range(1, arr_length+1) for j in range(0, arr_length-(i-1)))
            
                
# @lc code=end

