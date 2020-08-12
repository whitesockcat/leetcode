#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # sort by x_end
        points.sort(key = lambda x : x[1])

        ans = 1
        y0 = points[0][1]
        for x,y in points:
            if x>y0:
                ans += 1
                y0 = y
        return ans

# @lc code=end

