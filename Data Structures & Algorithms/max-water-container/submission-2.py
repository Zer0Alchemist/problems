class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left = 0
        right = len(heights) - 1

        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            val = width * height
            if val > maximum:
                maximum = val

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1

        return maximum