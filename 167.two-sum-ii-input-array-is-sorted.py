#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
# Your runtime beats 86.51 % of python3 submissions
# Your memory usage beats 5.8 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        idx1, idx2 = 0, len(numbers)-1

        while idx1 < idx2:
            
            sum_val = numbers[idx1] + numbers[idx2]

            if sum_val == target:
                return [idx1+1, idx2+1]
            elif sum_val < target:
                idx1 += 1
            else:
                idx2 -= 1
# @lc code=end

