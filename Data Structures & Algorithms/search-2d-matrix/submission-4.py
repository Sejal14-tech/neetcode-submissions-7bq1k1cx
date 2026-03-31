class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up = 0
        down = len(matrix)-1
        index=0
        while up<=down:
            mid = up + (down-up)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                left = 0
                right = len(matrix[0])-1
                while left<=right:
                    mid1 = left+(right-left)//2
                    if matrix[mid][mid1]==target:
                        return True
                    elif matrix[mid][mid1]>target:
                        right = mid1-1
                    else:
                        left = mid1+1
                return False
            elif matrix[mid][0]>target:
                down = mid-1
            else:
                up = mid+1
        return False
    
        