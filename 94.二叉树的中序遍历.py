#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # if not root:
        #     return []
        # res = []
        # res += self.inorderTraversal(root.left)
        # res += root.val
        # res += self.inorderTraversal(root.right)
        # return res  
        # # return [self.inorderTraversal(root.left)] + root.val + self.inorderTraversal(root.right)
        res, stack = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res
# @lc code=end

