class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix)-1
        index=0
        while up<=down:
            mid = up + (down-up)//2
            if matrix[mid][0]==target:
                return True
            elif matrix[mid][0]<target:
                index = mid
                up = mid+1
            else:
                down = mid-1
        print(index)
        left = 0
        right = len(matrix[0])-1
        while left<=right:
            mid = left+(right-left)//2
            if matrix[index][mid]==target:
                return True
            elif matrix[index][mid]>target:
                right = mid-1
            else:
                left = mid+1
        return False
        