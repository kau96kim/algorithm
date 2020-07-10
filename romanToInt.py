class Solution:
  def romanToInt(self, s: str) -> int:
    roman_numerals = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000
    }

    number = 0
    prev_number = 0
    romans = s[::-1]
    for roman in romans:
      roman_number = roman_numerals[roman]
      if prev_number > roman_number:
        number -= roman_number
      else:
        number += roman_number
      prev_number = roman_number

    return number

