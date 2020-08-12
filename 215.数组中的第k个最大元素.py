#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 快排
        # def quick_sort(nums, i, j, k):
        #     if i > j:
        #         return nums
        #     pivot = nums[i]
        #     low, high = i, j
        #     while i < j:
        #         while i < j and nums[j] < pivot:
        #             j -= 1
        #         nums[i] = nums[j]
        #         while i < j and nums[i] >= pivot:
        #             i += 1
        #         nums[j] = nums[i]
        #     nums[i] = pivot
        #     if i > k-1:
        #         quick_sort(nums, low, i-1, k)
        #     elif i < k-1:
        #         quick_sort(nums, i+1, high, k)
        #     else:
        #         return nums[k-1]
        #     return nums[k-1]
        # return quick_sort(nums, 0, len(nums)-1, k)

        # # 大顶堆
        # heapsize=len(nums)
        # def maxheap(a,i,length):
        #     l, r = 2*i +1, 2*i +2
        #     large = i
        #     if l<length and a[l] > a[large]:
        #         large = l
        #     if r<length and a[r] > a[large]:
        #         large = r
        #     if large != i:
        #         a[large], a[i] = a[i], a[large]
        #         maxheap(a,large,length)
        
        # for i in range(heapsize//2-1, -1, -1):
        #     maxheap(nums, i, heapsize)
        
        # for i in range(heapsize-1, heapsize-k, -1):
        #     nums[0], nums[i] = nums[i], nums[0]
        #     heapsize -= 1
        #     maxheap(nums, 0, heapsize)
        # return nums[0]


        # 替换nums[i]后维护最小堆：自顶向下调整新元素位置，直至该值满足(parent value < son value)
        def shift(i,k):
            flag=0
            while (i*2+1)<k and flag==0 :
                t=i
                if nums[t]>nums[2*i+1]:            
                    t=2*i+1
                if (i*2+2)<k and nums[t]>nums[2*i+2]  :            
                    t=2*i+2
                if t==i:
                    flag=1
                else :
                    nums[i],nums[t]=nums[t],nums[i]
                    i=t  
        
        #O(k):建立大小为K的最小堆， k/2-1是最后一个非叶节点，因为shift是向下调整，所以倒序从最下面出发，不然(4 32 1)->(2 34 1)->(2 14 3)->(2 14 3) 结果不对
        for i in range(k//2-1,-1,-1):
            shift(i,k)

        #O((N-k)logK)，剩余元素依次比较替换
        for i in range(k,len(nums)):
            if nums[0]<nums[i]:
                nums[0], nums[i]=nums[i], nums[0]
                shift(0,k)
        return nums[0]
        #sum=O(Nlogk-k(logK-1))
    



# @lc code=end

