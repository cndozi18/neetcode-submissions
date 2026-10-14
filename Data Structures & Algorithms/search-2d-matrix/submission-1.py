class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1 # rows
        lc, rc = 0, len(matrix[0]) - 1 # columns
        while lr < rr:
            mr = (lr + rr) // 2
            if target < matrix[mr][-1]:
                rr = mr
            elif target > matrix[mr][-1]:
                lr = mr + 1
            else:
                return True

        while lc <= rc:
            m = (lc + rc) // 2
            if target < matrix[lr][m]:
                rc = m - 1
            elif target > matrix[lr][m]:
                lc = m + 1
            else:
                return True
        return False