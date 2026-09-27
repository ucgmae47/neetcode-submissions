class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums, default=0)
        def robber(arr):
            arr[2] += arr[0]
            for i in range(3, len(arr)):
                arr[i] += max(arr[i-2], arr[i-3])
            return max(arr[-1], arr[-2])
        return max(robber(nums[:-1]), robber(nums[1:]))