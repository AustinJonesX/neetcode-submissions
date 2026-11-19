class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i, n in enumerate(nums):
        #     diff = target - n

        #     if diff in nums and i is not nums.index(diff):
        #         return sorted([i, nums.index(diff)])
                
        sorted_nums = []
        for i, num in enumerate(nums):
            sorted_nums.append([num, i])
        i, j = 0, len(nums) - 1

        while i < j:
            sum = sorted_nums[i][0] + sorted_nums[j][0]

            if sum == target:
                return[min(sorted_nums[i][1], sorted_nums[j][1]),
                max(sorted_nums[i][1], sorted_nums[j][1])]
            elif sum < target:
                i += 1
            else:
                j -= 1