#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = ListNode(0)
        p.next = head
        dummy = p
        # while head:
        #     while head.val == val:
        #         if head.next:
        #             head.val = head.next.val
        #             head.next = head.next.next
        #         else:
        #             p.next = None
        #             return dummy.next
        #     head = head.next
        #     p = p.next
        while p and p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dummy.next
                    
# @lc code=end

