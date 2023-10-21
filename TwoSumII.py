class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for indexSlow in range(0, n):
            indexFast = indexSlow + 1
            while (indexFast < n and numbers[indexSlow] + numbers[indexFast] <= target):
                if numbers[indexSlow] + numbers[indexFast] == target:
                    return [indexSlow + 1, indexFast + 1]
                indexFast += 1
