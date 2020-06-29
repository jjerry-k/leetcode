#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
# Your runtime beats 62.06 % of python3 submissions
# Your memory usage beats 28.41 % of python3 submissions (15.3 MB)
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return
        output = None
        while head:
            curr = head
            head = head.next
            curr.next = output
            output = curr
        return output
# @lc code=end