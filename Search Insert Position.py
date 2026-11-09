import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        indice = bisect.bisect_left(nums, target)
        if indice <= len(nums):
            return indice
        else:
            print(indice-1)

