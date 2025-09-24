class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        return str(x) == str(x)[::-1]    #[start:stop:step]



"""
s = "12345"
print("".join(reversed(s)))  # "54321"



s = "12345"
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s  # Baştan eklemek
print(reversed_s)  # "54321"



s = "12345"
print("".join(list(s)[::-1]))  # "54321"



s = "12345"
reversed_s = ""
i = len(s) - 1
while i >= 0:
    reversed_s += s[i]
    i -= 1
print(reversed_s)  # "54321"

"""



        