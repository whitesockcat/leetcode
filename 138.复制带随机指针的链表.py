#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
# """
# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
# """

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        while p:
            node = Node(p.val)
            node.next = p.next
            p.next = node
            p = node.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        pnewhead = head.next
        pold = head
        pnew = head.next
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return pnewhead
        
# @lc code=end

