class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ### Brute Force ###
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        
        return []

        ### Two Pointer ###
        # A = []
        # for i, n in enumerate(nums):
        #     A.append((n, i))
        # A.sort()

        # i, j = 0, len(nums)-1

        # while i < j:
        #     sum = A[i][0] + A[j][0]

        #     if sum == target:
        #         return [min(A[i][1], A[j][1]),
        #                 max(A[i][1], A[j][1])]
        #     elif sum < target:
        #         i += 1
        #     else:
        #         j -= 1
        
        # return []