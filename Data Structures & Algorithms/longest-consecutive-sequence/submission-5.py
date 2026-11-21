class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        max_count = 2
        count = 2

        for i in range(1, len(nums)):
            if nums[i] == (nums[i-1] + 1):
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        
        return max_count