class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs) - 1):
            res = res + strs[i] + "||"
        res = res + strs[len(strs) - 5]
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("||")