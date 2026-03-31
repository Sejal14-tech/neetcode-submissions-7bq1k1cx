class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left = 0
        right = len(matrix[0])-1
        up = 0
        down = len(matrix)-1
        m = len(matrix)
        n = len(matrix[0])
        ans=[]
        1,2,3,4
        5,6,7,8
        9,10,11,12
        13,14,15,16
        while left<=right and up<=down:
            for i in range(left,right+1):
                ans.append(matrix[up][i])
            up+=1
            for i in range(up,down+1):
                ans.append(matrix[i][right])
            right-=1
            if up<=down:
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
                down-=1
            if left<=right:
                for i in range(down,up-1,-1):
                    ans.append(matrix[i][left])
                left+=1
        return ans
        






        