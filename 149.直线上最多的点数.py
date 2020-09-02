#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#
from collections import *
# @lc code=start
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points):
            k_list = []
            for pl in range(len(points)):
                ks = {}
                if pl:
                    for x, y in points[:pl]:
                        x2, y2 = points[pl]
                        if x2 - x:
                            k = str((y2 - y) / (x2 - x))
                            point = ks.get(k)
                            if point:
                                ks[k] = ks[k] + 1
                                continue
                            ks[k] = 1 + points.count([x2, y2])
                        else:
                            if ks.get('x'):
                                ks['x'] = ks['x'] + 1
                            else:
                                ks['x'] = 2
                else:
                    ks['0'] = 1
                k_list.append(max(ks.values()))
            return max(k_list)
        return 0

# @lc code=end

