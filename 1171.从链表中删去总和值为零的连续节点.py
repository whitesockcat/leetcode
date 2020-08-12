#
# @lc app=leetcode.cn id=1171 lang=python3
#
# [1171] 从链表中删去总和值为零的连续节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        dummy.next = head
        s = 0
        s_sum = [s]
        vals = {}
        while p:
            s += p.val
            s_sum.append(s)
            if s not in vals:
                vals[s] = p
            else:
                vals[s].next = p.next
                s_sum.pop() # remove cur, keep the last
                while s_sum[-1] != s:
                    vals.pop(s_sum.pop())
            p = p.next
        return dummy.next
# @lc code=end

