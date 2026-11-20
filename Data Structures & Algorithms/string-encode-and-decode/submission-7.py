class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs)):
            if i is not (len(strs) - 1):
                res = res + strs[i] + "||"
            else:
                res = res + strs[i]
        return res

    def decode(self, s: str) -> List[str]:
        return s.split("||")