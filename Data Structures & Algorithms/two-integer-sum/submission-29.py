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
                break
            elif sum < target:
                i += 1
            else:
                j -= 1

        first_idx = nums.index(sorted_nums[i][0])
        second_idx = nums.index(sorted_nums[j][0], first_idx + 1)

        return [first_idx, second_idx]