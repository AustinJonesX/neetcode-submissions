class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        idx = 0
        result = []
        while idx < len(s):
            num_pref = ""
            while s[idx] != '#':
                num_pref = s[idx]
                idx += 1
                if idx >= len(s):
                    break
                    
            idx += 1

            char_cnt = int(num_pref)
            stop = char_cnt + idx

            while idx <= stop:
                word = ""
                word += s[idx]
                result.append(word)
                idx += 1
        idx += 1

        return result