class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort()
        for pivot in range(1, len(nums)):
            if nums[pivot] == nums[pivot - 1]:
                return nums[pivot]
        return -1