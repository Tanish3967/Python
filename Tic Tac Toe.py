board = ['', '', '', '', '', '', '', '', '']


def greet_player():
    print("Welcome to Tic Tac Toe")
    print("It's a two-player game\n")


def plyr_pos():
    choice = ''
    while choice not in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
        choice = input("Enter position number (0-8): ")

    return int(choice)


def game_board():
    print("Current Table-")
    for i in range(0, 9, 3):
        print(f"  {board[i]}|{board[i + 1]}|{board[i + 2]}")
        if i < 6:
            print("--------")


def gameon_choice():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input("Would you like to keep playing? Y or N ")

    return choice == "Y"


def plyr_choice_input(position):
    pos = input("Enter the Element: ")
    board[position] = pos


def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != '':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != '':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] != '' or board[2] == board[4] == board[6] != '':
        return True

    # Check if the board is completely filled
    if all(elem != '' for elem in board):
        return True

    return False


# main code
greet_player()

while True:
    game_board()
    position = plyr_pos()
    plyr_choice_input(position)
    game_board()

    if check_win():
        print("Congratulations! You won!")
        break

    if not gameon_choice():
        break

print("Thank you for playing Tic Tac Toe!")
