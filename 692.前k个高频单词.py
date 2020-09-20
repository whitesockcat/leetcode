#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
import collections
import heapq
# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = collections.Counter(words)
        s_count = sorted(count.items(), key=lambda x: (-x[1],x[0]))
        return [s_count.pop(0)[0] for _ in range(k)]

        # count = collections.Counter(words)
        # heap = [(-freq, word) for word, freq in count.items()]
        # heapq.heapify(heap)
        # return [heapq.heappop(heap)[1] for _ in range(k)]

# @lc code=end

