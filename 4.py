def check_win(board, row, current_col_index) -> bool:
    if sum(x == -1 for x in row) == 5:
        return True
    if sum(row[current_col_index] == -1 for row in board) == 5:
        return True
    return False

def mark_board(board: 'list[list[int]]', number:int) -> bool:
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == number:
                # mark row index with -1
                board[i][j] = -1
                # if and only if a new number is found in the board check if it's a winner row or column
                return check_win(board, row, j)
    return False

def winner_score(board: 'list[list[int]]', last_number_drawn:int) -> int:
    # sum per row and then sum the total of all rows 
    unmarked_total = sum(sum(filter(lambda x: x != -1, row)) for row in board)
    return unmarked_total * last_number_drawn

# read file
with open("4.txt") as file:
    bingo_numbers = list(map(int, next(file).split(",")))

    def into_matrix(raw):
        lines = raw.strip().splitlines()
        return list(list(map(int, row.split())) for row in lines)

    boards = list(map(into_matrix, file.read().split('\n\n')))


n_boards = len(boards)
n_won = 0

for number in bingo_numbers:
    for i, board in enumerate(boards):
        if board is None:
            continue

        if mark_board(board, number):
            n_won += 1
            if n_won == 1:
                first_winner_score = winner_score(board, number)
            elif n_won == n_boards:
                last_winner_score = winner_score(board, number)
            
            # eliminate board if it has won
            boards[i] = None


print(first_winner_score)
print(last_winner_score)