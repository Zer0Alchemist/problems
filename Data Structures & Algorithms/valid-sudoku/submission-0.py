class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        square = {i: set() for i in range(9)}

        for r in range(9):
            for c in range(9):
                box = r // 3 * 3 + c // 3
                if board[r][c] == ".":
                    continue

                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or 
                    board[r][c] in square[box]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[box].add(board[r][c])

        return True