class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i,j,k = 0, 1, len(nums) - 1
        res = set()
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            if total > 0:
                k -= 1
            elif total < 0:
                while total < 0 and j < k - 1:
                    j += 1
                    total = nums[i] + nums[j] + nums[k]
                while total > 0 and i < j - 1:
                    i += 1
                    total = nums[i] + nums[j] + nums[k]
            else:
                res.add((nums[i], nums[j], nums[k]))
                k -= 1
        return list(res)