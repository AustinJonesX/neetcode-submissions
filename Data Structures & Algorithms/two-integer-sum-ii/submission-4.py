class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i < j:
            total = numbers[j] + numbers[i]

            if total < target:
                i += 1
                continue
            elif total > target:
                j -= 1
            else:
                return [i+1,j+1]
        return []