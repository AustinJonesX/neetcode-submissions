class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ### Original attempt, no help

        # indices = {}
        # idx = 0
        # result = []

        # for i, s in enumerate(strs):
        #     freq = [0] * 26

        #     for c in s:
        #         freq[ord(c) - ord('a')] += 1

        #     freq = tuple(freq)

        #     if freq in indices:
        #         index = indices[freq]
        #         result[index].append(s)
        #     else:
        #         indices[freq] = idx
        #         idx += 1
        #         result.append([s])
        # return result

        ### Second attempt with more knowledge

        res = defaultdict(list)

        for i, s in enumerate(strs):
            freq = [0] * 26

            for c in s:
                freq[ord(c) - ord('a')] += 1

            freq = tuple(freq)

            res[freq].append(s)

        return list(res.values())