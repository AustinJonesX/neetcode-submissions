class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_table = {}
        t_table = {}

        for i in range(len(s)):
            if s[i] not in s_table:
                s_table[s[i]] = 1
            else:
                s_table[s[i]] = s_table.get(s[i]) + 1
            if t[i] not in t_table:
                t_table[t[i]] = 1
            else:
                t_table[t[i]] = t_table.get(t[i]) + 1

        if s_table == t_table:
            return True
        return False
