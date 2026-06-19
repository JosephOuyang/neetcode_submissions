from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = defaultdict(int)
        # loop through nums
        for i in range(len(nums)):
            currNum = nums[i]
            freqs[currNum] += 1
        majorityNum = len(nums) / 2
        # loop through freqs
        for num in freqs:
            if freqs[num] > majorityNum:
                return num

        