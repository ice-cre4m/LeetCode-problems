class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digit = [int(item) for item in digits]
        digit = int(''.join(map(str, digit)))
        digit = digit + 1
        return list(digit)