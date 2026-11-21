class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = "".join(filter(str.isalnum, s)).tolowercase()
        i, j = 0, len(string) - 1

        while i < j:
            if string[i] != string[j]:
                return False
            i += 1
            j -= 1
        
        return True