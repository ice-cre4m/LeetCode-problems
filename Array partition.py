class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort().reverse()
        for i in range(0, len(nums)-1, 2):
            maxSum += min(nums[i], nums[i+1])
            

