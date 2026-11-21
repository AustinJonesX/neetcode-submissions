class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(filter(str.isalnum(), s))
        return True