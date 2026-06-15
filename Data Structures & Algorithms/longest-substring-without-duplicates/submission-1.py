class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        for i in range(len(s)):
            repeated = set()
            currLongest = 0
            for j in range(i, len(s)):
                currChar = s[j]
                if currChar in repeated:
                    break
                else:
                    currLongest += 1
                    repeated.add(currChar)
            if currLongest > longest:
                longest = currLongest
        return longest


        