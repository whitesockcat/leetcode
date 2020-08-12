#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def dfs(root, sum, sum_t, path_t, ans):
            if not root:
                return ans
            sum_t += root.val
            path_t.append(root.val)
            if not (root.left or root.right):
                if sum_t == sum:
                    ans.append(copy.copy(path_t))
                # path_t.pop()
                # return ans
            else:
                dfs(root.left, sum, sum_t, path_t, ans)
                dfs(root.right, sum, sum_t, path_t, ans)
            path_t.pop()
            return ans
        return dfs(root, sum, 0, [], [])

# @lc code=end

