class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        l, r = 1, len(nums) - 1
        for i, n in enumerate(nums):
            if n > 0:
                break
            while l < r:
                if -n == nums[l] + nums[r]:
                    res.add((n, nums[l], nums[r]))
                    l += 1
        return list(res)
