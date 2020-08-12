#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
# @lc code=end

