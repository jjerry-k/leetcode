#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
# Your runtime beats 67.69 % of python3 submissions
# Your memory usage beats 5.67 % of python3 submissions (13.9 MB)
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = tmp = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry, val = divmod(v1 + v2 + carry, 10)
            tmp.next = ListNode(val)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            tmp = tmp.next
        return output.next
# @lc code=end

