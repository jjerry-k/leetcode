#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        answer = False
        sym2int = {"(":1, ")":1, "{":2, "}":2, "[":3, "]":3}
        converted = [sym2int[elem] for elem in s]
        print(converted)
        return answer
# @lc code=end

s = Solution()
print(s.isValid("{[]}()"))