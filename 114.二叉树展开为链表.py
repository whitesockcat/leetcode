#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if not root:
        #     return
        # queue = []
        # def dfs(root):
        #     if not root:
        #         return
        #     queue.append(root)
        #     dfs(root.left)
        #     dfs(root.right)
        # dfs(root)
        # head = queue.pop(0)
        # head.left = None
        # while queue:
        #     tmp = queue.pop(0)
        #     tmp.left = None
        #     head.right = tmp
        #     head = tmp

        while root:
            if root.left:
                subleft = root.left
                subright = subleft
                while subright.right:
                    subright = subright.right
                subright.right = root.right
                root.right = subleft
                root.left = None
            root = root.right

# @lc code=end

