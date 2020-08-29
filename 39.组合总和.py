#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def find(s, used, target):
            for i in range(s, len(candidates)):
                c = candidates[i]
                if c == target:
                    ans.append(used+[c])
                elif c < target:
                    find(i, used+[c], target-c)
                else:
                    return
        
        find(0, [], target)
        return ans

# @lc code=end

