#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(None)
        dummy.next = head
        p = dummy
        for i in range(n-1):
            head = head.next
        while head and head.next:
            p = p.next
            head = head.next
        p.next = p.next.next
        return dummy.next

# @lc code=end

