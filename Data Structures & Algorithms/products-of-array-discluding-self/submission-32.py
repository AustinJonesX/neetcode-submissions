class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        zero_idx = 0
        for i, n in enumerate(nums):
            if n == 0:
                zero_cnt += 1
                zero_idx = i
            else:
                product *= n
        
        if zero_cnt > 1:
            return [0] * len(nums)
        elif zero_cnt == 1:
            res = [0] * len(nums)
            res[zero_idx] = product
            return result

        
        result = []
        for n in nums:
                result.append(product // nums)
        
        return result