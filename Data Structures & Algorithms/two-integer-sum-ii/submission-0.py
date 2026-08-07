class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        set_numbers = set(numbers)
        for i, num in enumerate(numbers):
            if target - num in set_numbers:
                j = i + 1
                while j < len(numbers):
                    if numbers[j] == target - num:
                        return [i+1, j+1]
                    j += 1