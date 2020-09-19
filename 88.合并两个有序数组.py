#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # # 双指针 从前往后
        # nums1_copy = nums1[:m]
        # nums1[:] = [] # 必须这么写 参见https://leetcode-cn.com/problems/merge-sorted-array/solution/gelthin-gui-bing-pai-xu-by-gelthin/
        # p1, p2 = 0, 0
        # while p1<m and p2<n:
        #     if nums1_copy[p1]<nums2[p2]:
        #         nums1.append(nums1_copy[p1])
        #         p1 += 1
        #     else:
        #         nums1.append(nums2[p2])
        #         p2 += 1
        # while p1<m:
        #     nums1.append(nums1_copy[p1])
        #     p1 += 1
        # while p2<n:
        #     nums1.append(nums2[p2])
        #     p2 += 1

        # 双指针 从后往前
        p1,p2,p = m-1,n-1,m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]>nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        nums1[:p2+1] = nums2[:p2+1]
# @lc code=end

