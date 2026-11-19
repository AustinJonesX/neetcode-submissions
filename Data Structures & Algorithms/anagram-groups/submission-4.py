class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = {}
        idx = 0
        result = []

        for i, s in enumerate(strs):
            freq = {}

            for c in s:
                freq[c] = 1 + freq.get(s, 0)

            if freq in indices:
                result[indices[freq]].append(s)
            else:
                indices[freq] = idx
                idx += 1
                result.append(s)
        return result