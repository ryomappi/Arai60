import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        # 頻度を負にしてmin-heapで最大ヒープを模倣
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        out = []
        for _ in range(k):
            _, num = heapq.heappop(heap)
            out.append(num)
        return out


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [num for num, _ in Counter(nums).most_common(k)]
