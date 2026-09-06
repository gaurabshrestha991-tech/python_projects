# Sudoku Solver

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def display_board():
    print()
    
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
            
        for column in range(9):
            if column % 3 == 0 and column != 0:
                print("|", end=" ")
                
            print(board[row][column], end=" ")
            
        print()
        
def find_empty_cell():
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return row, column
    return None

def is_valid(number, row, column):
    
    for i in range(9):
        if board[row][i] == number:
            return False
        
    for i in range(9):
        if board[i][column] == number:
            return False
        
    box_row = (row // 3) * 3
    box_column = (column // 3) * 3
    
    for i in range(box_row, box_row + 3):
        for j in range(box_column, box_column + 3):
            if board[i][j] == number:
                return False
            
    return True

def solve_sudoku():
    
    empty_cell = find_empty_cell()
    
    if empty_cell is None:
        return True
    
    row, column = empty_cell
    
    for number in range(1, 10):
        
        if is_valid(number, row, column):
            
            board[row][column] = number
            
            if solve_sudoku():
                return True
            
            board[row][column] = 0
            
    return False

print("Orginal Sudoku:")
display_board()

if solve_sudoku():
    print("\nSolved Sudoku:")
    display_board()
else:
    print("\nNo solution exists.")
        