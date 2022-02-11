from cmath import inf

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = 'X'
com = 'O'

# (COM) win = 10 lose = -10 tie = 0
scores = {
    'com': 10,
    'you': -10,
    'tie': 0
}


def drawBoard(board):
    for i in range(3):
        if i == 1 or i == 2:
            print("-----------")
        for j in range(3):
            if j == 1 or j == 2:
                print(" | ", end="")
            if(j == 0):
                print(" ", end="")
            print(board[i][j], end="")

        print()


def convert_pos(pos):
    # from 1-3
    if pos <= 3:
        return 0, pos - 1
    # from 4-6
    elif pos <= 6:
        return 1, pos - 4
    # from 7-9
    else:
        return 2, pos - 7


# def go_to_pos(board, turn, player_pos):
#     x, y = convert_pos(player_pos)

#     board[x][y] = turn


def win_check(board):
    # win check

    # horizontal
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != " ":
            who_win = board[i][0]
            if who_win == "X":
                return [1, 'you']
            else:
                return [1, 'com']

    # vertical
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != " ":
            who_win = board[0][i]
            if who_win == "X":
                return [1, 'you']
            else:
                return [1, 'com']

    # diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ":
        who_win = board[0][0]
        if who_win == "X":
            return [1, 'you']
        else:
            return [1, 'com']
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != " ":
        who_win = board[0][2]
        if who_win == "X":
            return [1, 'you']
        else:
            return [1, 'com']
    # draw check
    arr = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != " ":
                arr.append([i, j])
    if len(arr) == 9:
        return [1,'tie']

    return [0, ""]
 
# AI
def find_best_move(board):
    bestScore = -float(inf)
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = com
                score = minimax(board,0,False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    move = [i,j]
    try:    
        board[move[0]][move[1]] = com
    except Exception:
        pass

def minimax(board,depth,isMinimizing):
    win_check_arr = win_check(board)
    if win_check_arr[1] != "":
        score = scores[win_check_arr[1]]
        if win_check_arr[1] == "com": # win
            return score - depth
        elif win_check_arr[1] == "you": # lose
            return score + depth
        else:
            return score

    if isMinimizing:
        bestScore = -float(inf)
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = com
                    score = minimax(board,depth + 1,False)
                    board[i][j] = " "
                    bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float(inf)
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player
                    score = minimax(board,depth + 1,True)
                    board[i][j] = " "
                    bestScore = min(score,bestScore)
        return bestScore

def main():
    playing = True
    drawBoard(board)
    print("Tic Tac Toe (1 Player)")
    while playing:
        player_pos = int(input('Enter your position (1-9): '))
        # go_to_pos(board, player, player_pos)   
        x,y = convert_pos(player_pos)
         # if position is not empty, type again
        while True:
            if board[x][y] == " ":
                board[x][y] = player
                break
            print("Unavailable Spot!")
            player_pos = int(input('Enter your position (1-9): '))
            x,y = convert_pos(player_pos)
        find_best_move(board)
        drawBoard(board)
        win_check_arr = win_check(board)
        if win_check_arr[0]:
            if win_check_arr[1] == "you":
                print("You Win!")
                break
            if win_check_arr[1] == "com":
                print("You Lose!")
                break
            else:
                print("It's a tie!")
                break


if __name__ == '__main__':
    main()
