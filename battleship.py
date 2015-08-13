from random import randint

def print_board(board):
    print "  1 2 3 4 5"
    count = 0
    for row in board:
        count += 1
        print str(count) + " " + " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def make_ships(number):
    ships = []
    while len(ships) < number:
        ship_row = random_row(board)
        ship_col = random_col(board)
        if [ship_row, ship_col] not in ships:
            ships.append([ship_row, ship_col])
    return ships

def check(row, col, ships):
    for coord in ships:
        if row == coord[0] and col == coord[1]:
            return True
    return False

answer = "yes"

while answer.lower() == "yes" or answer.lower() == "y":
    board = []

    for x in range(5):
        board.append(["O"] * 5)

    print "Let's play Battleship!"
    print_board(board)

    ships = make_ships(3)

    turn = 0

    while turn <= 4:
        print "Turn", turn + 1
        # Everything from here on should go in your for loop!

        guess_row = int(raw_input("Guess Row(1 to 5):")) - 1
        guess_col = int(raw_input("Guess Col(1 to 5):")) - 1

        if check(guess_row, guess_col, ships):
            print "Congratulations! You sunk my battleship!"
            break
        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed my battleship!"
                board[guess_row][guess_col] = "X"
                turn += 1
        print_board(board)

    if turn == 5:
        print "Game Over"
    answer = raw_input("Would you like to play game?")
