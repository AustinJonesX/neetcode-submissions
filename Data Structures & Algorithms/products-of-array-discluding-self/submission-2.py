class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for n in nums:
            product *= n
        
        result = []
        for i, n in enumerate(nums):
            if nums[i] == 0:
                result.append(product)
                continue
            result.append(product // nums[i])
        
        return result