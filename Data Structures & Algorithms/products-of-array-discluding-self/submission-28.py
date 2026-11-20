class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i, j = 1, len(nums)
        prefix, suffix = [0] * len(nums), [0] * len(nums)

        while i < len(nums) - 1:
            prefix[i] = nums[i] * nums[i-1]
            suffix[j] = nums[j] * nums[j-1]
            i += 1
            j -= 1
        
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(prefix[1])
            elif i == len(nums) - 1:
                res.append(suffix[len(nums) - 1])
            else:
                res.append(prefix[i-1] * suffix[i+1])
        
        return res