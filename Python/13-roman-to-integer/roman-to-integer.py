class Solution:
    def romanToInt(self, s: str) -> int:
        #Roman numerals are written largest to smallest from left to right.
        #Largest to smallest: addition
        #Smaller before larger: subtract smaller

        romanToInt = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M": 1000}
        sol = 0

        for i in range(len(s) - 1):
            if romanToInt[s[i]] < romanToInt[s[i+1]]:
                sol -= romanToInt[s[i]] 
            else:
                sol += romanToInt[s[i]]

        sol += romanToInt[s[-1]]
        return sol
