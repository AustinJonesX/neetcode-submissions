class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {int}

        for n in nums:
            freq[n] += 1

        srt_pairs = []
        for key, value in freq.items():
            srt_pairs.append((value, key))
        
        srt_pairs.sort()

        result = []
        for i in range(k):
            result.append(srt_pairs[i][0])

        return result