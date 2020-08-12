#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if intervals == []: return 0
        ## 根据区间右端点排序
        intervals = sorted(intervals, key=lambda x: x[1])
        num = 0
        compare = intervals[0]
        for interval in intervals[1:]:
            if interval[0] < compare[1]:
                num += 1
            else:
                compare = interval
        return num

# @lc code=end

