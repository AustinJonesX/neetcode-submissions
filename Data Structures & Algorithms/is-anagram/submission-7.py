class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = (list(s)).sort()
        list2 = (list(t)).sort()

        if list1.join() == list2.join():
            return True
        return False