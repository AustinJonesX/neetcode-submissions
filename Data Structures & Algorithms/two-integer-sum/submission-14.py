class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i, n in enumerate(nums):
        #     diff = target - n

        #     if diff in nums and i is not nums.index(diff):
        #         return sorted([i, nums.index(diff)])
                
        sorted_nums = sorted(nums)