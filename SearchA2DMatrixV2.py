class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        return self.bSearchMatrix(matrix, target, (0,0), (m,n))

    def bSearchMatrix(self, matrix: List[List[int]], target:int, left:tuple, right:tuple) -> bool:
        while left[0] <= right[0] and left[1] <= right[1]:
            middle = ((left[0]+left[0])//2, (right[1]+right[1])//2)
            if matrix[middle[0]][middle[1]] > target:
                right = (middle[0], middle[1] - 1)
            elif matrix[middle[0]][middle[1]] < target:
                left = (middle[0], middle[1] + 1)
            else:
                return True
        return False