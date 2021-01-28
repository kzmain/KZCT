class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        list_len = len(nums)
        for pivot in range(list_len):
            num = nums[pivot]
            for sub_pivot in range(pivot, list_len):
                if num == nums[sub_pivot]:
                    return num
        return -1