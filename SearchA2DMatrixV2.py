class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        return self.bSearchMatrix(matrix, target, (0,0), (m,n))

    def bSearchMatrix(self, matrix: List[List[int]], target:int, left:tuple, right:tuple) -> bool:
        while left[0] <= right[0] and left[1] <= right[1]:
            middle = ((left[0]+left[0])//2, (right[1]+right[1])//2)
            if matrix[middle[0]][middle[1]] > target:
                if middle[1] != 0: #not frist element in row
                    right = (middle[0], middle[1] - 1)
                else:
                    right = (middle[0]-1, len(matrix[0]))
            elif matrix[middle[0]][middle[1]] < target:
                if middle[1] != len(matrix[0]) - 1: #not last element in row
                    left = (middle[0], middle[1] + 1)
                else:
                    left = (middle[0]+1, 0)
            else:
                return True
        return False