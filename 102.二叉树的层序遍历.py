#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        # ans = []
        # queue = [root]
        # while queue:
        #     size = len(queue)
        #     tmp = []
        #     for _ in range(size):
        #         r = queue.pop(0)
        #         tmp.append(r.val)
        #         if r.left:
        #             queue.append(r.left)
        #         if r.right:
        #             queue.append(r.right)
        #     ans.append(tmp)
        # return ans

        ans = []
        def dfs(idx, r):
            if len(ans) < idx:
                ans.append([])
            ans[idx-1].append(r.val)
            if r.left:
                dfs(idx+1, r.left)
            if r.right:
                dfs(idx+1, r.right)
        dfs(1,root)
        return ans
# @lc code=end

