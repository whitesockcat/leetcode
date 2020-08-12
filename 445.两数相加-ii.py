#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 翻转
        # def reverse(head):
        #     p = None
        #     while head:
        #         # head.next, p, head = p, head, head.next
        #         t = head.next
        #         head.next = p
        #         p = head
        #         head = t
        #     return p
        # l1 = reverse(l1)
        # l2 = reverse(l2)
        # b = 0
        # d = dummy = ListNode(None)
        # while l1 or l2 or b: # 注意 or b
        #     t1 = l1.val if l1 else 0
        #     t2 = l2.val if l2 else 0
        #     a, b = (t1 + t2 + b)%10, (t1 + t2 + b)//10
        #     d.next = ListNode(a)
        #     d = d.next
        #     l1 = l1.next if l1 else None           
        #     l2 = l2.next if l2 else None
        # return reverse(dummy.next)

        # 栈
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        b = 0
        d = None
        while s1 or s2 or b: # 注意 or b
            try:
                t1 = s1.pop()
            except:
                t1 = 0
            try:
                t2 = s2.pop()
            except:
                t2 = 0
            a, b = (t1 + t2 + b)%10, (t1 + t2 + b)//10
            cur = ListNode(a)
            cur.next = d
            d = cur
        return cur

# @lc code=end

