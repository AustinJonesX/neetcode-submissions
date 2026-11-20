class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0] * n
        suff = [0] * n
        res = [0] * n

        pref[0] = 1
        suff[n - 1] = 1

        for i in range(1, len(n-1)):
            pref[i] = num[i - 1] * pref[i - 1]
        
        for i in range(len(n) - 2, 0, -1):
            suff[i] = num[i + 1] * suff[i + 1]

        for i in range(len(n)):
            res[i] = pref[i] * suff[i]

        return res