class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0
        for start in nums:
            if start - 1 not in set_nums:
                end = start
                while end in set_nums:
                    end += 1
                length = end - start
                if length > longest:
                    longest = length
        return longest