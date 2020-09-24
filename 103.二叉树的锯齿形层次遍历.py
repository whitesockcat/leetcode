#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res = []
        cur_level = [root]
        depth = 0
        while cur_level:
            tmp = []
            next_level = []
            for node in cur_level:
                tmp.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            if depth % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)
            depth += 1
            cur_level = next_level
        return res

        # res = []
        
        # def helper(root, depth):
        #     if not root: return 
        #     if len(res) == depth:
        #         res.append([])
        #     if depth % 2 == 0:res[depth].append(root.val)
        #     else: res[depth].insert(0, root.val)
        #     helper(root.left, depth + 1)
        #     helper(root.right, depth + 1)
        # helper(root, 0)
        # return res
        
# @lc code=end

