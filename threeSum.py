class Solution:
  def threeSum(self, nums: [int]) -> [[int]]:
    answer = []

    nums.sort()
    negative = [x for x in nums if x < 0]
    positive = [x for x in nums if x > 0]
    zero = True if 0 in nums else False

    if zero:
      for x in negative:
        if abs(x) in positive:
          answer.append([0, x, abs(x)])
          print(answer)

    print(answer)

Solution.threeSum(Solution, [-2, 0, 1, 2])