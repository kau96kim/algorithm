class Solution:
    def reverseString(self, s: [str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        length = len(s) // 2
        for i in range(length):
            alphabet = s[i]
            s[i] = s[-1-i]
            s[-1 - i] = alphabet

