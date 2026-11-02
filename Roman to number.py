class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        diccRomanSimbols = {
            "I": 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for index in range(0, len(s)):
            if index >= len(s)-1:
                number += diccRomanSimbols[s[index]]
            else:
                if  diccRomanSimbols[s[index]] < diccRomanSimbols[s[index + 1]]:
                    number -=  diccRomanSimbols[s[index]]
                else:
                    number += diccRomanSimbols[s[index]]
            print(number)

        return number
         
print(Solution.romanToInt(Solution, "MCMXCIV"))
#Giving a roman Number convert it to integer