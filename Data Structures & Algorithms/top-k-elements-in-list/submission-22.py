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
        # freq = defaultdict(int)

        # for n in nums:
        #     freq[n] += 1

        # minHeap = []

        # for key, value in freq.items():
        #     heapq.heappush(minHeap, (value, key))
        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)
        
        # result = []
        # while minHeap:
        #     result.append(heapq.heappop(minHeap)[1])
        # return result

        ### Bucket Sort
        count = {}
        maxFreq = 0

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            maxFreq = max(maxFreq, count[num])
        
        freq = [[] for _ in range(maxFreq + 1)]

        for num, count in count.items():
            freq[count].append(num)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
