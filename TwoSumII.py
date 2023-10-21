class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        leftPointer = 0
        rightPointer = n-1

        while leftPointer <= rightPointer:
            sum = numbers[leftPointer] + numbers[rightPointer]
            if sum < target:
                leftPointer +=1
            elif sum > target:
                rightPointer-=1
            else:
                return [leftPointer+1, rightPointer+1]
