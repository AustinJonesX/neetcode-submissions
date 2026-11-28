class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i, n in enumerate(nums):
            if n > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[l] + nums[r]
                if -n == total:
                    res.add((n, nums[l], nums[r]))
                elif -n > total:
                    r -= 1
                else:
                    l += 1
                
        return list(res)
