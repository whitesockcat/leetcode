#
# @lc app=leetcode.cn id=817 lang=python3
#
# [817] 链表组件
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        SET_G = set(G)
        h = head
        count = 0
        while h:
            if h.val in SET_G:
                if (h.next and h.next.val not in SET_G or 
                    not h.next):
                    count += 1
            h = h.next
        return count
# @lc code=end

