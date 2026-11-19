class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### Sorting
        # freq = defaultdict(int)

        # for n in nums:
        #     freq[n] += 1

        # srt_pairs = []
        # for key, value in freq.items():
        #     srt_pairs.append((value, key))
        # srt_pairs.sort(reverse=True)

        # result = []
        # for i in range(k):
        #     result.append(srt_pairs[i][1])

        # return result

        ### Min Heap
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        minHeap = []

        for key, value in freq.items():
            heapq.heappush(minHeap, (value, key))
            if len(minHeap) > k:
                minHeap.pop()
        
        result = []
        while minHeap:
            result.append(minHeap.pop()[1])
        return result