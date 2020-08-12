#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # res, stack = [], [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         res.append(node.val)
        #         if node.children:
        #             for child in node.children:
        #                 stack.append(child)
        # return res[::-1]

        res, stack = [], root and [(root, False)]
        while stack:
            node, flag = stack.pop()
            if flag and node:
                res.append(node.val)
            else:
                stack.append((node, True))
                if node:
                    stack.extend((n, False) for n in reversed(node.children))
        return res
# @lc code=end

