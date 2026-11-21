class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = 1
        res = [1] * n

        for i in range(n):
            res[i] *= pref
            pref *= nums[i]
        return res