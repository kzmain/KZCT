class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        tmp_set = set()
        for num in nums:
            if num in tmp_set:
                return num
            tmp_set.add(num)
        return -1