#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        # if not root:
        #     return []
        # res = [root.val]
        # for child in root.children:
        #     res += self.preorder(child)
        # return res
        res, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                for i in range(1, len(node.children)+1, 1):
                    stack.append(node.children[-i])
        return res
# @lc code=end

