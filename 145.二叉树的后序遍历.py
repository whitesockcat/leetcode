#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # res, stack = [], [root]
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         res.append(node.val)
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return res[::-1]

        # res, stack, node, last = [], [], root, None
        # while stack or node:
        #     if node:
        #         stack.append(node)
        #         node = node.left
        #     else:
        #         node = stack[-1]
        #         if not node.right or last == node.right:
        #             node = stack.pop()
        #             res.append(node.val)
        #             last = node
        #             node = None
        #         else:
        #             node = node.right

        # res, stack = [], [(root, False)]
        # while stack:
        #     node, visited = stack.pop()
        #     if node:
        #         if visited:
        #             res.append(node.val)
        #         else:
        #             stack.append((node, True))
        #             stack.append((node.right, False))
        #             stack.append((node.left, False))                
        # return res

        ans = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)
        dfs(root)
        return ans
# @lc code=end

