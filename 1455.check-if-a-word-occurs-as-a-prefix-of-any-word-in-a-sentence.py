#
# @lc app=leetcode id=1455 lang=python3
#
# [1455] Check If a Word Occurs As a Prefix of Any Word in a Sentence
# Why..?

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        for idx, word in enumerate(sentence.split(" ")):
            if word.startswith(searchWord):
                return idx + 1 #index + 1 acc to question
            else:
                continue
        return -1
# @lc code=end