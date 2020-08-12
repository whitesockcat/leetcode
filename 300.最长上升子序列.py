#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # if n == 0: return 0
        # dp = [1] * n
        # ans = 1
        # for i in range(n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #             ans = max(ans, dp[i])
        # return  ans

        if(not nums):
            return 0
        n=len(nums)
        if(n<2):
            return n
        tail=[nums[0]]
        for i in range(1,n):
            if(nums[i]>tail[-1]):
                tail.append(nums[i])
                continue
            l=0
            r=len(tail)-1
            while l <= r:
                mid = (l+r)//2
                if tail[mid] >= nums[i]:
                    r = mid -1
                else:
                    l = mid +1
            tail[l] = nums[i]
        return len(tail)



# @lc code=end

