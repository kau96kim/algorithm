class Solution:
  def longestPalindrome(self, s: str) -> str:
    def commonString(firstString: str) -> str:
      total_length = len(firstString)
      common_string = ""
      length = 0
      for i in range(0, total_length):
        for j in range(total_length+1, i + length, -1):
          substring = firstString[i:j]
          if substring == substring[::-1] and length < (j-i):
            length = j-i
            common_string = firstString[i:j]
            continue

      return common_string

    return commonString(s)
