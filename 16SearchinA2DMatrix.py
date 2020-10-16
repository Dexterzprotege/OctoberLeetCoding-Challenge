'''Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 
Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false

Example 3:
Input: matrix = [], target = 0
Output: false
 
Constraints:
m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-104 <= matrix[i][j], target <= 104'''

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix)==0:
            return False
        row, col = len(matrix), len(matrix[0])
        rowStart, rowEnd = 0, row-1
        while rowStart < rowEnd:
            mid = (rowStart + rowEnd + 1) >> 1
            if matrix[mid][0] == target:
                return True
            if target < matrix[mid][0]:
                rowEnd = mid-1
            else:
                rowStart = mid
        start, end = 0, col-1
        while start<=end:
            mid = (start + end)>>1
            if matrix[rowStart][mid] == target:
                return True
            if target < matrix[rowStart][mid]:
                end = mid-1
            else:
                start = mid+1
        return False
