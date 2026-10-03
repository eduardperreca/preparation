class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix)-1
        pick = -1
        while top <= bottom:
            row = (top + bottom) // 2
            if matrix[row][0] <= target <= matrix[row][-1]:
                pick = row
                break
            if target < matrix[row][0]:
                bottom = row - 1
            else:
                top = row + 1        
        l, r = 0, len(matrix[pick])-1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[pick][m]:
                return True
            if target > matrix[pick][m]:
                l = m + 1
            else:
                r = m -1
        return False