import math

board = [" " for _ in range(9)]

def display_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()
    
def check_winner(player):
    winning_combinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]
    
    for combination in winning_combinations:
        if all(board[index] == player for index in combination):
            return True
        
    return False

def is_board_full():
    return " " not in board

def get_available_moves():
    return [i for i in range(9) if board[i] == " "]

def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    
    if check_winner("X"):
        return -1
    
    if is_board_full():
        return 0
    
    if is_maximizing:
        best_score = -math.inf
        
        for move in get_available_moves():
            board[move] = "O"
            
            score = minimax(False)
            
            board[move] = " "
            
            best_score = max(best_score, score)
            
        return best_score
    else:
        best_score = math.inf
        
        for move in get_available_moves():
            board[move] = "X"
            
            score = minimax(True)
            
            board[move] = " "
            
            best_score = min(best_score, score)
        
        return best_score
    
def ai_move():
    best_score = -math.inf
    best_move = None
    
    for move in get_available_moves():
        board[move] = "O"
        
        score = minimax(False)
        
        board[move] = " "
        
        if score > best_score:
            best_score = score
            best_move = move
            
    board[best_move] = "O"
    
    print(f"Computer chose position {best_move + 1}")
    
def player_move():
    while True:
        try:
            position = int(input("Enter your position (1-9): ")) - 1
            
            if position < 0 or position > 8:
                print("Pleas enter a number between 1 and 9.")
                
            elif board[position] != " ":
                print("That position is already occupied.")
                
            else:
                board[position] = "X"
                break
            
        except ValueError:
            print("Please enter a valid number.")
            
def display_positions():
    print("Position Guide:")
    print()
    print("1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()

def play_game():
    print("=" * 35)
    print("TIC TAC TOE AI")
    print("=" * 35)
    
    print("\nYou are X")
    print("Computer is O\n")
    
    display_positions()
    
    while True:
        display_board()
        
        player_move()
        
        if check_winner("X"):
            display_board()
            print("Congratulation! You have won!")
            break
        
        if is_board_full():
            display_board()
            print("It's a draw!")
            break
        
        print("\nComputer is thinking....")
        ai_move()
        
        if check_winner("O"):
            display_board()
            print("Computer Won!")
            break
        
        if is_board_full():
            display_board()
            print("It's a draw!")
            break
        
play_game()