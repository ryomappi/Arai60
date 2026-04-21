import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hq = []
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.hq, val)
        if len(self.hq) > self.k:
            heapq.heappop(self.hq)
        return self.hq[0]
