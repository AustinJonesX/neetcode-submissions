class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            target = target - n

            if target in nums:
                result = []
                result.append(i)
                result.append(nums.index(target))
                return result