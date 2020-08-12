#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                while head != s:
                    head = head.next
                    s = s.next
                return s
        return None
        
# @lc code=end

