#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = ListNode(None)
        fast = ListNode(None)
        slow.next = head
        fast.next = head
        h = head
        if not head:
            return None
        else:
            while fast and fast.next:
                slow, fast = slow.next, fast.next.next
                if not fast:
                    break
            pre = None
            h2 = slow.next
            slow.next = None
            while h2:
                t = h2.next
                h2.next = pre
                pre = h2
                if t:
                    h2 = t
                else:
                    break
            while h and h2:
                t1 = h.next
                h.next = h2
                t2 = h2.next
                h2.next = t1
                h = t1
                h2 = t2
            return head
                
                

# @lc code=end

