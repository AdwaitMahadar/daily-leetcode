class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            # Calculate the current area
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width

            # Update the maximum area if the current area is greater
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area