class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sort first solution
        sortedNums = sorted(nums)
        for i in range(len(sortedNums) - 1):
            if sortedNums[i] == sortedNums[i + 1]:
                return True
        return False
        