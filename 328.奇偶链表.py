#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # even = ListNode(None)
        # even.next = head
        # even_start = even
        # odd = ListNode(None)
        # odd.next = even
        # while odd and odd.next:
        #     # print('odd', odd.val, 'even', even.val)
        #     if odd.next.next:
        #         odd.next = odd.next.next
        #     else:
        #         break
        #     if even and even.next:
        #         even.next = even.next.next
        #     odd = odd.next
        #     even = even.next
        # odd.next = even_start.next
        # return head
        if not head:
            return None
        odd = head
        even_h = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
        odd.next = even_h
        return head

# @lc code=end

