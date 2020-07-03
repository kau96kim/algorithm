class Solution:
  def maxArea(self, height: [int]) -> int:
    i, j = 0, len(height) - 1
    max_area = 0

    while i < j:
      min_height = min(height[i], height[j])
      max_area = max(max_area, min_height * (j-i))

      if height[i] < height[j]:
        i += 1
      else:
        j -= 1

    return max_area
