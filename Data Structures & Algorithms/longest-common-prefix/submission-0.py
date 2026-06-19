class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]
        for i in range(len(first), 0, -1):
            subString = first[ : i]
            matches = 0
            for j in range(len(strs)):
                if not strs[j].startswith(subString):
                    break
                matches += 1
            if matches == len(strs):
                return subString
        return ""
            

        