#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Why..?

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        output = -1
        for idx, word in enumerate(sentence.split(" ")):
            if searchWord in word:
                output = idx + 1
                break
        return output
# @lc code=end