class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts = {}

        for i in range(len(nums)):
            if nums[i] in dicts:
                return [dicts.get(nums[i]),i]
            else:
                dicts[target - nums[i]] = i