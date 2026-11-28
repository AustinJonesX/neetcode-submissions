class Solution:
    def trap(self, height: List[int]) -> int:
        pref_max = [0] * len(height)
        suff_max = [0] * len(height)
        total = 0

        max_h = height[0]
        for i in range(1, len(height)):
            max_h = max(max_h, height[i])
            pref_max[i] = max_h

        max_h = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            max_h = max(max_h, height[i])
            suff_max[i] = max_h

        for i in range(1, len(height) - 1):
            total += max(min(pref_max[i], suff_max[i]) - height[i], 0)
        return total