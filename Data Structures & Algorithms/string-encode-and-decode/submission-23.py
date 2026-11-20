class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "EMPTY"

        res = strs[0]
        for i in range(1, len(strs), 1):
            res = res + "||" + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("||")
        
        if res == ["EMPTY"]:
            return []

        return res