#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack, res = [], [prices[i] for i in range(n)]
        for i in range(n):
            while stack and prices[stack[-1]] >= prices[i]:
                res[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return res

# @lc code=end

