import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        indice = bisect.bisect_left(nums, target)
        if nums[indice] == target:
            print(indice)
        else:
            print(indice+1)


nums = [1,3,5,6]
target = 3

indice = bisect.bisect_left(nums, target)
print(indice)