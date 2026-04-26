class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_cap = sum(weights)
        left = 1
        right = max_cap
        cap = float("inf")
        while left <= right:
            mid = (left + right) // 2
            # Confirm mid cap ships within days
            d = 1
            load = 0
            for w in weights:
                if load + w <= mid:
                    load += w
                elif load + w > mid and w <= mid:
                    d += 1
                    load = w
                else:
                    d = float("inf")
                    break
            if d > days:
                left = mid + 1
            else:
                cap = min(cap, mid)
                right = mid - 1

        return cap
