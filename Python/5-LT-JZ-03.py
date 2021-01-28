class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        tmp_dict = {}
        for num in nums:
            if num not in tmp_dict.keys():
                tmp_dict[num] = 1
            else:
                return num
        return -1