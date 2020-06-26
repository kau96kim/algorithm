class Solution:
  def myAtoi(self, str: str) -> int:
    def compare_range(result:int) -> int:
      minimum = -2 ** 31
      maximum = 2 ** 31 - 1
      if result < minimum:
        return minimum
      elif result > maximum:
        return maximum
      return result
    
    signList = ["+", "-"]
    sign = ""
    
    for element in str.split():
      try:
        return compare_range(int(element))
      except:
        try:
          if element[0] in signList:
            sign = element[0]
            element = element[1:]
          return compare_range(int(sign + element.replace(element.lstrip("1234567890"), "")))
        except:
          return 0
    
    return 0
