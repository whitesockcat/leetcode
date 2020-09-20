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
        # # 会报凑
        # count = collections.Counter(words)
        # candidates = count.keys()
        # candidates.sort(key = lambda w: (-count[w], w))
        # return candidates[:k]

        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

# @lc code=end

