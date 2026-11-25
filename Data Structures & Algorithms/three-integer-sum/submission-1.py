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
                if i == j-1:
                    j += 1
                else:
                    i += 1
            else:
                res.add([nums[i], nums[j], nums[k]])
                k -= 1
        return res