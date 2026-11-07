class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        indicesToRemove = [] 
        for x in range(len(nums)):  
            if nums[x] == val:
                indicesToRemove.append(x)

        for indice in sorted(indicesToRemove, reverse=True):
            nums.pop(indice)
            
        return len(nums)