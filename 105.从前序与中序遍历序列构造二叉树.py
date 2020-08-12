#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(pl:int, pr:int, il:int, ir:int):
            if pl>pr or il>ir:
                return None
            p_root = pl
            i_root = index[preorder[p_root]]
            root = TreeNode(preorder[p_root])
            left_size = i_root-il
            root.left = myBuildTree(pl+1, pl+left_size,
                                    il, i_root-1)
            root.right = myBuildTree(pl+left_size+1, pr,
                                    i_root+1, ir)
            return root
        index = {element: i for i, element in enumerate(inorder)}
        n = len(preorder)
        return myBuildTree(0,n-1,0,n-1)
# @lc code=end

