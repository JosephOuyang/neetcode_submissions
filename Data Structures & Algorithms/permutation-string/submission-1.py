class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # loop through all the substrings in s2
        sortedS1 = sorted(s1)
        len1, len2 = len(s1), len(s2)
        for i in range(len2 - len1 + 1):
            if sorted(s2[i : i + len1]) == sortedS1:
                return True
        return False

