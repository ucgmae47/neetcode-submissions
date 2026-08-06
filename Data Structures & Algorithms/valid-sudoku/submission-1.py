class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = 0
        while row < 9:
            col = 0
            while col < 9:
                cur = board[row][col]
                if cur != '.':
                    for i in range(9):
                        if i == col:
                            continue
                        if board[row][i] == cur:
                            return False
                    for i in range(9):
                        if i == row:
                            continue
                        if board[i][col] == cur:
                            return False
                    r = (row // 3) * 3
                    c = (col // 3) * 3
                    for i in range(3):
                        for j in range(3):
                            if r+i == row and c+j == col:
                                continue
                            if board[r+i][c+j] == cur:
                                return False
                col += 1
            row += 1
        return True