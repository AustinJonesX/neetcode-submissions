class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            product *= n
        
        result = []
        for i, n in enumerate(nums):
            result.append(product // nums[i])
        
        return result