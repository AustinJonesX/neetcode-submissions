class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            diff = target - n

            if diff in nums and i is not nums.index(diff):
                return [i, nums.index(diff)]
                