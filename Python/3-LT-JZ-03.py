class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        for pivot in range(len(nums)):
            while pivot != nums[pivot]:
                tmp_val = nums[pivot]
                if tmp_val == nums[tmp_val]:
                    return tmp_val
                # important 注意怎么交换的
                nums[pivot], nums[tmp_val] = nums[tmp_val], nums[pivot]
        return -1