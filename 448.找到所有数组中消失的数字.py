#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # hash_table = {}
        # n = len(nums)
        # for num in nums:
        #     hash_table[num] = 1
        # result = []
        # for i in range(1,n+1):
        #     if i not in hash_table:
        #         result.append(i)
        # return result

        # # 为了不占空间 改了输入 
        # for num in nums:
        #     idx = abs(num) -1
        #     if nums[idx] > 0:
        #         nums[idx] *= -1
        # ans = []
        # n = len(nums)
        # for i in range(n):
        #     if nums[i]>0:
        #         ans.append(i+1)
        # return ans
        
        def swap(nums, index1, index2):
            # 这一步是必要的，否则会使得一个数变成 0
            if index1 == index2:
                return
            nums[index1] = nums[index1] ^ nums[index2]
            nums[index2] = nums[index1] ^ nums[index2]
            nums[index1] = nums[index1] ^ nums[index2]
        n = len(nums)
        for i in range(n):
            # print(i)
            while nums[i] != nums[nums[i] -1]:
                # print(nums[i], nums[nums[i] -1])
                idx = nums[i] -1
                swap(nums, i, idx)
                # nums[i],nums[idx]=nums[idx],nums[i]
        ans = []
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans

# @lc code=end

