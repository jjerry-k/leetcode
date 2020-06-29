#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
# Your runtime beats 79.19 % of python3 submissions
# Your memory usage beats 74.09 % of python3 submissions (29 MB)
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None

        p = headA
        while p.next:
            p = p.next
        mark = p
        #make a cycled list
        mark.next = headA
        
        rst = None
        p1 = headB
        p2 = headB
        while p1 and p2:
            p1 = p1.next
            p2 = p2.next
            if p2: p2 = p2.next
            if p1 == p2: break

        if p1 and p2 and p1 == p2:
            p1 = headB
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            rst = p1

        #unmake the cycle
        mark.next = None

        return rst
# @lc code=end