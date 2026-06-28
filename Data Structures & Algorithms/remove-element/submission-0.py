class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        sameCount = 0
        for i in range(len(nums) - 1, -1, -1):
            currNum = nums[i]
            if currNum == val:
                nums.pop(i)
                sameCount += 1
        return length - sameCount
        