#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 缺失数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # hash_table = {}
        # for num in nums:
        #     hash_table[num] = 1
        # for i in range(len(nums)+1):
        #     if i not in hash_table:
        #         return i

        # nums.sort()
        # n = len(nums)
        # for i in range(n+1):
        #     if i==n or i != nums[i]:
        #         return i
        
        # ans = len(nums)
        # for i, num in enumerate(nums):
        #     ans ^= i ^ num
        # return ans

        n = len(nums)
        expected_sum = n*(n+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

# @lc code=end

