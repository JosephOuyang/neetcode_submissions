class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window techinque
        left = 0
        repeated = set()
        longest = 0
        for right in range(len(s)):
            while s[right] in repeated:
                repeated.remove(s[left])
                left += 1
            repeated.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
        
        