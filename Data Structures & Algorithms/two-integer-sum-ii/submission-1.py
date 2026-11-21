class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            diff = numbers[j] - numbers[i]

            if diff < target:
                i += 1
                continue
            elif diff > target:
                j -= 1
            else:
                return [i,j]