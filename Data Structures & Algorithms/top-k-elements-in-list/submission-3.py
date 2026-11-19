class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = ['a'] * len(nums)
        count = 0
        currNum = nums[0]

        for i in range(len(nums)):
            if currNum == nums[i]:
                count += 1
            else:
                buckets[count] = currNum
                currNum = nums[i]
                count = 0
            i += 1

        frequent = len(nums) - 1
        answer = []
        while k != 0:
            if buckets[frequent] != 'a':
                answer.append(buckets[frequent])
                k -= 1
            frequent -= 1

        return answer



        