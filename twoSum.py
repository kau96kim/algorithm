class Solution:
  def twoSum(self, nums: [int], target: int) -> [int]:
    def getIndex(ascNums: [int], target: int) -> [int]:
      for num in ascNums:
        try:
          index = ascNums.index(target - num)
          return num, ascNums[index]
        except:
          continue

    min, max = getIndex(sorted(nums), target)
    return [nums.index(min), len(nums) - nums[::-1].index(max) - 1]
