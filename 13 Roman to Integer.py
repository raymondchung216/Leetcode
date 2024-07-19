class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        total = 0
        prev = -1
        for letter in s:
            if roman[letter] <= prev:
                total += count
                count = 0
                count += roman[letter]
            else:
                count = roman[letter] - count
            prev = roman[letter]
        total += count
        return total
