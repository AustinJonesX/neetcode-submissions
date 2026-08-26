class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            sorted_chars = ''.join(sorted(word))
            if sorted_chars in anagrams:
                anagrams[sorted_chars].append(word)
            else:
                anagrams[sorted_chars] = [word]
        
        result = []
        for values in anagrams.values():
            result.append(values)
            
        return result