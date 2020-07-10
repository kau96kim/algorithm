class Solution:
  def longestCommonPrefix(self, strs: [str]) -> str:
    def getCommonPrefix(firstWord: str, secondWord: str) -> str:
      common_prefix = ""
      for x in firstWord:
        if x == secondWord[:1]:
          common_prefix += x
        else:
          return common_prefix
        secondWord = secondWord[1:]
      return common_prefix

    prefix = strs[0] if strs else ""
    for word in strs:
      prefix = getCommonPrefix(prefix, word)

    return prefix
