#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
# Your runtime beats 23.65 % of python3 submissions
# Your memory usage beats 21.7 % of python3 submissions (14 MB)
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        arr1, arr2 = '', ''
        while l1 or l2:
            if l1 : 
                arr1 += str(l1.val)
                l1 = l1.next
            if l2 :
                arr2 += str(l2.val)
                l2 = l2.next
        
        total = str(int(arr1) + int(arr2))
        dummy = ListNode(0)
        cur_node = dummy
        for i in total:
            cur_node.next = ListNode(int(i))
            cur_node = cur_node.next
        return dummy.next 
# @lc code=end