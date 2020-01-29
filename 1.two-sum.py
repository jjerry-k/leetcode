#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = None
        bkpoint = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                # print(nums[i]+nums[j])
                if nums[i]+nums[j] == target:
                    #print(nums[i]+nums[j])
                    answer = [i, j]
                    bkpoint = 1
                    break
            if bkpoint == 1:
                break
        return answer
# @lc code=end