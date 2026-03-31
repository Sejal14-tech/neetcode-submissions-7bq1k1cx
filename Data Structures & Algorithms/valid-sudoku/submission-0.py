class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]
        for i in range(len(board)):
            for j in  range(len(board[0])):
                box_index = (i//3)*3+(j//3)
                if board[i][j]=='.':
                    continue
                elif board[i][j] in row[i]:
                    return False
                elif board[i][j] in col[j]:
                    return False
                elif board[i][j] in box[box_index]:
                    return False
                else:
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[box_index].add(board[i][j])
        return True


