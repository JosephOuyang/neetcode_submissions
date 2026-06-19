class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # optimized solution
        majorityElem, count = 0, 0
        for num in nums:
            if count == 0:
                majorityElem = num
            if majorityElem == num:
                count += 1
            else:
                count -= 1
        return majorityElem
        