class Solution:
  def reverse(self, x: int) -> int:
    def compare_range(result:int) -> int:
      minimum = -2 ** 31
      maximum = 2 ** 31 - 1
      if result < minimum:
        return 0
      elif result > maximum:
        return 0
      return result

    sign = '+' if x >= 0 else '-'
    reversed_int = int(sign + str(abs(x))[::-1])
    return compare_range(reversed_int)


