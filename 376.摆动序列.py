#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#

# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1
            if nums[i] < nums[i - 1]:
                down = up + 1
        return max(up, down)
        
# @lc code=end

