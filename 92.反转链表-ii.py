#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = p = ListNode(None)
        dummy.next = head
        p.next = head
        for i in range(1, n+1):
            if i < m:
                p = head
                head = head.next
            elif i == m:
                t = s = head
                head = head.next
            else:
                # print(head.val)
                next_tmp = head.next
                head.next = s
                # print(head.val, '->', s.val)
                s = head
                head = next_tmp
        t.next = head
        p.next = s
        return dummy.next
# @lc code=end

