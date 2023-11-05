# slow since O(m+log n)
# v2 is faster
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowCounter = 0
        m = len(matrix)
        n = len(matrix[0])

        while rowCounter < m:
            if matrix[rowCounter][0]<= target and matrix[rowCounter][n-1]>= target:
                return self.bSearch(matrix[rowCounter], 0, n-1, target)
            else:
                rowCounter += 1
        return False


    def bSearch(self, arr, left, right, target) -> bool:
        while left <= right:
            middle = (left + right)//2
            if arr[middle] > target:
                right = middle - 1
            elif arr[middle] < target:
                left = middle + 1
            else:
                return True
                print("test")
        return False