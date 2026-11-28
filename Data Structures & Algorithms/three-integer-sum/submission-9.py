class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = 0, 0, len(nums) - 1
        l, r = i, k
        loop_count = 0
        sum = 0
        res = []
        nums.sort()

        while nums[r] >= 0 and nums[l] < 0:
            i = l
            j = l + 1
            k = r
            while sum <= 0 and l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    j = l
                    k = r
                    res.append([i,j,k])
                l += 1
            if (i + r) >= 0:
                r -= 1
            else:
                l = i + 1
        
        return res