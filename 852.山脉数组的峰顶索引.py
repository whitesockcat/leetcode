#
# @lc app=leetcode.cn id=852 lang=python3
#
# [852] 山脉数组的峰顶索引
#

# @lc code=start
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # for i in range(len(A)-1):
        #     if A[i+1] < A[i]:
        #         return i
        
        n = len(A)
        m = n//2
        l,r = 0,n-1
        while 1:
            if m == 0 or m == n-1:
                return m
            elif A[m]>A[m+1] and A[m]>A[m-1]:
                return m
            elif A[m]>A[m+1] and A[m]<A[m-1]:
                r = m
                m = (m-l)//2 + l
            elif A[m]<A[m+1] and A[m]>A[m-1]:
                l = m
                m = (r-m)//2 + m
            else:
                return False

        # lo, hi = 0, len(A) - 1
        # while lo < hi:
        #     mi = (lo + hi) // 2
        #     if A[mi] < A[mi + 1]:
        #         lo = mi + 1
        #     else:
        #         hi = mi
        # return lo


# @lc code=end

