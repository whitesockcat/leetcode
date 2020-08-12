#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # one = two = ListNode(None)
        # two.next = head
        # one.next = two
        # if head:
        #     if head.next:
        #         root = head.next
        #     else:
        #         return head
        # else:
        #     return head
        # while head and head.next:
        #     one.next = head.next
        #     two.next = one
        #     t = head.next.next
        #     one = head
        #     two = head.next
        #     head = t
        # if head:
        #     one.next = head
        #     two.next = one
        # else:
        #     one.next = None
        #     two.next = one
        # return root
        thead = ListNode(-1)
        thead.next = head
        c = thead
        while c.next and c.next.next:
            a, b=c.next, c.next.next
            c.next, a.next = b, b.next
            b.next = a
            c = c.next.next
        return thead.next
# @lc code=end

