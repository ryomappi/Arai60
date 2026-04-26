class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        while True:
            mid = (left + right) // 2
            if nums[mid] >= nums[left] and nums[mid] <= nums[right]:
                return nums[left]
            if mid == left:
                return nums[right]

            if nums[mid] < nums[left]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid
