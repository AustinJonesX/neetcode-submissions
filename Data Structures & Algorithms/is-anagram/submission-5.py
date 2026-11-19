class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = (list(s)).sort()
        list2 = (list(t)).sort()

        if list1 == list2:
            return True
        return False