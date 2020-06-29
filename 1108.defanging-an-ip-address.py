#
# @lc app=leetcode id=1108 lang=python3
#
# [1108] Defanging an IP Address
# Your runtime beats 91.25 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "[.]".join(address.split("."))
# @lc code=end

