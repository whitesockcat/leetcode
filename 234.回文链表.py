#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        FLAG = True
        even = False
        slow = fast = head
        pre = ListNode(None)
        pre.next = head
        while fast and fast.next:
            fast = fast.next.next
            t = slow.next
            slow.next = pre
            pre = slow
            slow = t
        fliphead = slow
        if fast: # 奇数
            slow = slow.next
        while slow:
            if slow.val != pre.val:
                FLAG = False
            t = pre.next
            pre.next = fliphead
            fliphead = pre
            pre = t
            slow = slow.next
        return FLAG

            
# @lc code=end

