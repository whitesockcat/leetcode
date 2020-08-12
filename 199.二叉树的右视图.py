#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def dfs(root, stack, depth):
            # stack = [(root.val, 1)]
            if root:
                if len(stack) < depth:
                    stack.append(root.val)
                dfs(root.right, stack, depth+1)
                dfs(root.left, stack, depth+1)
            return stack
        stack = []
        depth = 1
        return dfs(root, stack, depth)
# @lc code=end

