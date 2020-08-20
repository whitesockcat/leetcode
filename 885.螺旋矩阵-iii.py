#
# @lc app=leetcode.cn id=885 lang=python3
#
# [885] 螺旋矩阵 III
#

# @lc code=start
class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ans = []
        x = r0
        y = c0
        dx = 0
        dy = 1
        flags = 1
        while len(ans)<R*C:
            for _ in range(2):
                for _ in range(flags):
                    if 0 <= x < R and 0 <= y < C:
                        ans.append([x, y])
                    x += dx
                    y += dy
                dx,dy=dy,-dx

            flags += 1
        return ans



        
# @lc code=end

