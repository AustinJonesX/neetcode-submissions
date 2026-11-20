class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(s) - 1):
            res = res + s + "||"
        res = res + strs[len(strs) - 1]
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("||")