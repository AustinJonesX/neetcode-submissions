class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = 1
        res = [1] * n

        for i in range(n):
            res[i] = pref
            pref *= nums[i]
        post = 1
        for i in range(n-1, 0, -1):
            res[i] *= post
            post *= nums[i] * res[i]
        return res