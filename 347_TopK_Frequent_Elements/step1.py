import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        inv_d = defaultdict(list)
        for key in d:
            inv_d[d[key]].append(key)

        freqs = [i for i in inv_d]
        heapq.heapify_max(freqs)
        out = []
        while len(out) < k:
            key = heapq.heappop_max(freqs)
            out += inv_d[key]
        return out
