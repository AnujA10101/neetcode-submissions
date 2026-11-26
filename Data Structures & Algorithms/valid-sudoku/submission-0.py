class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            seen_row = set()
            for num in row:
                if num == ".":
                    continue
                if num in seen_row:
                    return False
                seen_row.add(num)
        

        for col in zip(*board):
            seen_col = set()
            for num in col:
                if num == ".":
                    continue
                if num in seen_col:
                    return False
                seen_col.add(num)
        
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                seen_sq = set()

                for row in range(start_row, start_row + 3):
                    for col in range(start_col, start_col + 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in seen_sq:
                            return False
                        seen_sq.add(board[row][col])
        return True



       

        