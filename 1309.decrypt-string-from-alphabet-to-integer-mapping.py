#
# @lc app=leetcode id=1309 lang=python3
#
# [1309] Decrypt String from Alphabet to Integer Mapping
# Your runtime beats 86.31 % of python3 submissions
# Your memory usage beats 23.5 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def freqAlphabets(self, s: str) -> str:
        dic = {
            '1':'a','2':'b','3':'c','4':'d','5':'e',
            '6':'f','7':'g','8':'h','9':'i','10#':'j',
            '11#':'k','12#':'l','13#':'m','14#':'n','15#':'o',
            '16#':'p','17#':'q','18#':'r','19#':'s','20#':'t',
            '21#':'u','22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
        
        for key in list(dic.keys())[::-1]:
            if key in s: 
                s = s.replace(key, dic[key])
        
        return s
# @lc code=end