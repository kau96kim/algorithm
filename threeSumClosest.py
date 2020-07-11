class Solution:
    def threeSumClosest(self, nums: [int], target: int) -> int:
      answer = 0
      gap = 2 * pow(10, 4)
      nums.sort()
      length = len(nums)
      for i, i_value in enumerate(nums):
        j, k = i + 1, length - 1

        while j < k:
          sum = nums[j] + nums[k] + i_value
          if sum == target:
            return target
          elif sum < target:
            j += 1
          elif sum > target:
            k -= 1
          
          if gap > abs(target - sum):
            gap = abs(target - sum)  
            answer = sum
          
      return answer
