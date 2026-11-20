class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        for n in nums:
            if n == 0:
                zero_cnt += 1
                continue
            product *= n
        
        if zero_cnt > 1:
            return [0] * len(nums)
        
        result = []
        for i, n in enumerate(nums):
            if nums[i] == 0:
                if zero_cnt < 1:
                    result.append(product)
                continue
            elif zero_cnt > 1:
                result.append(0)
            result.append(product // nums[i])
        
        return result