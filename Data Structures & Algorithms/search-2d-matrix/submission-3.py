class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                mid_l = 0
                mid_r = len(matrix[mid]) - 1

                while mid_l <= mid_r:
                    mid_i = (mid_l + mid_r) // 2

                    if matrix[mid][mid_i] == target:
                        return True

                    if matrix[mid][mid_i] > target:
                        mid_r = mid_i - 1
                    else:
                        mid_l = mid_i + 1
                
                return False

        return False
        