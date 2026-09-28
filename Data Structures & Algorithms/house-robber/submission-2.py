class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums, default=0)
        back_2 = back_1 = 0
        for curr in nums:
            new = max(back_2 + curr, back_1)
            back_2 = back_1
            back_1 = new
        return back_1