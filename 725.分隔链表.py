#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        h = root
        l = 0
        while h:
            l += 1
            h = h.next
        h = root
        parts = []
        if k >= l:
            stride = 1
            while h:
                t = h.next
                h.next = None
                parts.append(h)
                h = t
            null_num = k - len(parts)
            for i in range(null_num):
                parts.append(None)
        else:
            stride = l // k
            remainder = l % k
            for i in range(k):
                abstride = stride
                hh = h
                if remainder:
                    abstride += 1
                    remainder -= 1
                for j in range(1, abstride):
                    h = h.next
                t = h.next
                h.next = None
                parts.append(hh)
                h = t
        return parts
        
# @lc code=end

