class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    def maxLength(word: str) -> int:
      count = 0
      length = 0
      new_word = ""
      for char in word:
        if char in new_word:
          new_word = new_word[new_word.index(char)+1:] + char
          count = len(new_word)
        else:
          new_word += char
          count += 1
        length = count if count > length else length

      return length

    return maxLength(s)
