class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left = max_right = 0
        amt = 0

        while left <= right:
            if height[left] <= height[right]:
                if height[left] < max_left:
                    amt += max_left - height[left]
                else:
                    max_left = height[left]
                left += 1
            else:
                if height[right] < max_right:
                    amt += max_right - height[right]
                else:
                    max_right = height[right]
                right -= 1
        
        return amt