class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = (list(s)).sort()
        list2 = (list(t)).sort()

        if list1.toString() == list2.toString():
            return True
        return False