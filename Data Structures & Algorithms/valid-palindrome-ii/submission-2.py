class Solution:
    def validPalindrome(self, s: str) -> bool:
        # two pointer solution
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                noLeft, noRight = s[l + 1 : r + 1], s[l : r]
                if noLeft == noLeft[::-1] or noRight == noRight[::-1]:
                    return True
                else:
                    return False
            l, r = l + 1, r - 1
        return True
        