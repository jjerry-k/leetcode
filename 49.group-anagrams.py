#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
# Your runtime beats 5.35 % of python3 submissions
# Your memory usage beats 83.02 % of python3 submissions (15.8 MB)

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_strs = set(["".join(sorted(i)) for i in strs])
        sorted_strs = ["".join(sorted(i)) for i in strs]
        output = []
        for item in set_strs:
            sub_output = []
            while sorted_strs.count(item) > 0:
                i = sorted_strs.index(item)
                sub_output.append(strs[i])
                strs.pop(i)
                sorted_strs.pop(i)
            output.append(sub_output)
        
        return output
# @lc code=end