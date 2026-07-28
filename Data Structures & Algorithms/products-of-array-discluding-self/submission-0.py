class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = nums.count(0)
        if count > 1:
            return [0] * len(nums)
        if count == 1:
            index = nums.index(0)
            nums = [x for x in nums if x != 0]
            for num in nums:
                product *= num
            res = [0] * (len(nums)+1)
            res[index] = product
            return res
        for num in nums:
            product *= num
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            res[i] = product // num
        return res