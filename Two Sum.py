# Solucion optimizada para el problema O(n)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


# Solucion del problema menos eficiente O(n^2)

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                sum = nums[x] + nums[y]
                if sum == target:
                    result = [x,y]
                    return result
                else:
                    continue
            