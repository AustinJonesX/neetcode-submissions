class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort(s)
        sort(t)

        if s == t:
            return True
        return False