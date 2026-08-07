class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        max = 0
        while i < j:
            area = (j-i) * min(heights[i], heights[j])
            if area > max:
                max = area
            if heights[i] < heights[j]:
                x = i+1
                while x < j and heights[x] <= heights[i]:
                    x += 1
                i = x
            else:
                x = j-1
                while i < x and heights[x] <= heights[j]:
                    x -= 1
                j = x

        return max
        