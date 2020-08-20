#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []
        ans = [[0]*n for _ in range(n)]
        cnt = 0
        i, j = 0, -1
        judge = 1
        while n > 0:
            for _ in range(n):
                cnt += 1
                j += judge * 1
                ans[i][j] = cnt
            
            for _ in range(n-1):
                cnt += 1
                i += judge * 1
                ans[i][j] = cnt
            n -= 1
            judge *= -1

        return ans
# @lc code=end

