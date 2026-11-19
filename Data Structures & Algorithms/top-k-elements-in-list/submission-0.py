class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [0] * nums.len()