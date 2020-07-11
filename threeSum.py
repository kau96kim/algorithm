class Solution:
  def threeSum(self, nums: [int]) -> [[int]]:
    # O(n^3) version 1
    # answer = set()
    # for i, first_value in enumerate(nums):
    #   for j, second_value in enumerate(nums[i+1:]):
    #     for third_value in nums[i+j+2:]:
    #       if first_value + second_value + third_value == 0:
    #         element = sorted([first_value, second_value, third_value])
    #         answer.add(tuple(element))

    answer = set()
    nums.sort()
    length = len(nums)
    for i, i_value in enumerate(nums):
      j, k = i + 1, length - 1

      while j < k:
        sum = nums[j] + nums[k] + i_value
        if sum == 0:
          element = sorted([i_value, nums[j], nums[k]])
          answer.add(tuple(element))
          j += 1
          k -= 1
        elif sum < 0:
          j += 1
        elif sum > 0:
          k -= 1
        
    return answer
