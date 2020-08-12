#
# @lc app=leetcode.cn id=1299 lang=python3
#
# [1299] 将每个元素替换为右侧最大元素
#

# @lc code=start
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack = [-1]
        for i in range(len(arr)-1, -1, -1):
            t = arr[i]
            arr[i] = stack[-1]
            if t > stack[-1] or len(stack) == 1:
                stack.append(t)
        return arr

# @lc code=end

