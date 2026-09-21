class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        mid = (low + high) // 2
        while not high < low:
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
            mid = (low + high) // 2
        return -1