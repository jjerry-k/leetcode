#
# @lc app=leetcode id=1290 lang=python3
#
# [1290] Convert Binary Number in a Linked List to Integer
# Your runtime beats 92.54 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.1 MB)
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        output = 0
        while head:
            output = (output<<1) | head.val
            head = head.next
        return output

# @lc code=end