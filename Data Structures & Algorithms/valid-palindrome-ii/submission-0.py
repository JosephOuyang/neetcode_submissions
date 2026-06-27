class Solution:
    def validPalindrome(self, s: str) -> bool:
        reversedString = s[::-1]
        if s == reversedString:
            return True
        for i in range(len(s)):
            newString = s[ : i] + s[i + 1 : ]
            if newString == str(newString[::-1]):
                return True
        return False


        