from random import randint

BOARD_SIZE = 7

def print_board(board1, board2):
    print "     Board 1             Board 2"
    print "  1 2 3 4 5 6 7       1 2 3 4 5 6 7 "
    count = 0
    for i in range(BOARD_SIZE):
        count += 1
        row1 = board1[i]
        row2 = board2[i]
        print str(count) + " " + " ".join(row1) + "     " + str(count) + " " + " ".join(row2)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def check_side(row, col, ships, board):
    positions = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
    available_positions = []
    for position in positions:
        if position not in ships and position[0] >= 0 and position[1] >=0 and position[0] < len(board) and position[1] < board[1]:
            available_positions.append(position)
    return available_positions

def make_ships(number, board):
    ships = []
    while len(ships) < number*2:
        ship_row = random_row(board)
        ship_col = random_col(board)
        if [ship_row, ship_col] not in ships:
            available_positions = check_side(ship_row, ship_col, ships, board)
            if len(available_positions) != 0:
                ships.append([ship_row, ship_col])
                ships.append(available_positions[randint(0, len(available_positions)-1)])
    return ships

def check(row, col, ships):
    for coord in ships:
        if row == coord[0] and col == coord[1]:
            return True
    return False

answer = "yes"

while answer.lower() == "yes" or answer.lower() == "y":
    board1 = []
    board2 = []

    for x in range(BOARD_SIZE):
        board1.append(["O"] * BOARD_SIZE)
        board2.append(["O"] * BOARD_SIZE)

    print "\n\nLet's play Battleship!\n"
    print_board(board1, board2)

    ships1 = make_ships(3, board1)
    ships2 = make_ships(3, board2)

    turn = 0

    while turn <= 9:
        print "\nTurn", (turn + 2) / 2
        if turn % 2 == 0:
            name = "Player 1"
            ships = ships1
            board = board1
        else:
            name = "Player 2"
            ships = ships2
            board = board2

        while True:
            guess_row = raw_input(name + ", Guess Row(1 to 7):")
            if len(guess_row) == 1:
                break
        guess_row = int(guess_row) - 1

        while True:
            guess_col = raw_input(name + ", Guess Col(1 to 7):")
            if len(guess_col) == 1:
                break
        guess_col = int(guess_col) - 1

        if check(guess_row, guess_col, ships):
            print "Congratulations! " + name + " win!"
            break
        else:
            if (guess_row < 0 or guess_row > BOARD_SIZE - 1) or (guess_col < 0 or guess_col > BOARD_SIZE - 1):
                print "Oops, that's not even in the ocean."
            elif(board[guess_row][guess_col] == "X"):
                print "You guessed that one already."
            else:
                print "You missed battleship!"
                board[guess_row][guess_col] = "X"
                turn += 1
        print_board(board1, board2)

    if turn == 10:
        print "Game Over"
    answer = raw_input("Would you like to play game?")
