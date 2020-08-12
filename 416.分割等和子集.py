#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums=sum(nums)
        if sums%2==1:
            return False
        target=sums//2
        dp=[False for _ in range(target+1)]
        dp[0]=True
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j]=dp[j] or dp[j-nums[i]]
        return dp[-1]

# @lc code=end

