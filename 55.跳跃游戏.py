#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i<= rightmost:
                rightmost = max(rightmost, i+nums[i])
            else:
                return False
        return True

# @lc code=end

