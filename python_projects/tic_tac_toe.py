board = [" " for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
    
def show_positions():
    print("Board Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

def check_winner(player):
    winning_combinations = [
         [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    
    for combination in winning_combinations:
        if (
            board[combination[0]] == player
            and board[combination[1]] == player
            and board[combination[2]] == player
        ):
            return True
        
    return False
    
def check_draw():
    return " " not in board

def play_game():
    current_player = "x"
    
    print("====== TIC TAC TOE ======")
    show_positions()
    
    while True:
        display_board()
        
        try:
            position = int(
                input(f"player {current_player}, enter position (1-9): ")
            )
            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue
            index = position - 1
            
            if board[index] != " ":
                print("That position is already occupied.")
                continue
            board[index] = current_player
            
            if check_winner(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break
            if check_draw():
                display_board()
                print("The game is a draw!")
                break
            if current_player == "x":
                current_player = "o"
            else:
                current_player = "x"
        except ValueError:
            print("Invalid input! Please enter a number.")
        
play_game()
            