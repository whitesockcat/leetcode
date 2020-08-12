#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # 我的dp
        # if amount == 0: return 0
        # dp = {k:1 for k in coins}
        # for i in range(1, amount+1):
        #     if i in dp.keys():
        #         continue
        #     t = []
        #     for j in coins:
        #         m = i - j
        #         if m in dp.keys():
        #             t.append(dp[m])
        #     t.sort()
        #     if t:
        #         dp[i] = t[0] + 1
        # if amount in dp.keys():
        #     return dp[amount]
        # else:
        #     return -1

        # dp
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 

# @lc code=end

