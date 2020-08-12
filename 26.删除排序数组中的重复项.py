#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # x = 1
        # for i in range(len(nums)-1):
        #     if nums[i] != nums[i+1]:
        #         nums[x] = nums[i+1]
        #         x += 1
        # return x
        if not nums:    return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i+1
# @lc code=end

