class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = sort(list(s))
        list2 = sort(list(t))

        if list1 == list2:
            return True
        return False