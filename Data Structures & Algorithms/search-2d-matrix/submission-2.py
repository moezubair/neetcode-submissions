class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        n = rows*columns - 1 

        l, r = 0, n

        while l<=r:
            mid = l + (r - l) // 2
            mid_i = mid // columns
            mid_j = mid % columns
            if matrix[mid_i][mid_j] == target:
                return True
            elif matrix[mid_i][mid_j] < target:
                # Move to the right
                l = mid + 1
            else:
                r = mid - 1
        return False