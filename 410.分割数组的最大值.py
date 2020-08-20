#
# @lc app=leetcode.cn id=410 lang=python3
#
# [410] 分割数组的最大值
#

# @lc code=start
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # dp
        # n = len(nums)
        # f = [[10**18] * (m + 1) for _ in range(n + 1)]
        # sub = [0]
        # for elem in nums:
        #     sub.append(sub[-1] + elem)
        # # print(sub)
        # f[0][0] = 0
        # for i in range(1, n + 1):
        #     for j in range(1, min(i, m) + 1):
        #         for k in range(i):
        #             f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
        
        # return f[n][m]

        # 二分
        def check(x: int) -> bool:
            total, cnt = 0, 1
            for num in nums:
                if total + num > x:
                    cnt += 1
                    total = num
                else:
                    total += num
            return cnt <= m


        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left

# @lc code=end

