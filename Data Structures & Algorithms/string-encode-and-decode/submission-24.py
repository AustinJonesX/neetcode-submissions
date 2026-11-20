class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        
        return res

    def decode(self, s: str) -> List[str]:
        return [s]
