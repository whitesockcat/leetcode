#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre = pre_s = ListNode(None)
        big = big_s = ListNode(None)
        while head:
            if head.val < x:
                pre.next = head
                pre = pre.next
            else:
                big.next = head
                big = big.next
                
            head = head.next
        big.next = None
        pre.next = big_s.next
        return pre_s.next

# @lc code=end

