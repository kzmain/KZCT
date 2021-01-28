class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = (high + low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot 
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]