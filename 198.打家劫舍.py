#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # n = len(nums)
        # if n==1:    return nums[0]
        # if n==2:    return max(nums[0], nums[1])
        # dp = {}
        # dp[1] = nums[0]
        # dp[2] = max(nums[0], nums[1])
        # for i in range(3, n+1):
        #     dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        # return dp[n]

        # dp 滚动数组
        if not nums:
            return 0

        size = len(nums)
        if size == 1:
            return nums[0]
        
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            first, second = second, max(first + nums[i], second)
        
        return second

# @lc code=end

