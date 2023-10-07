import os
import time
"""
$ stands for player, B stands for Box, . stands for goal, # stands for obstacle
8 for moving up, 2 for moving down, 4 for moving left, 6 for moving right
"""
def readGame():
    file_path = './game.txt'
    with open(file_path, 'r') as file:

        content = file.read()
        #print(content)

    matrix = matrix = [[0 for _ in range(7)] for _ in range(7)]
    for row in range(7):
        for col in range(7):
            matrix[row][col] = content[(row%7)*7 + col + (row%7)]
    #print(matrix)
    return matrix

def plotCanvas(matrix):
    for row in matrix:
        st = ''
        for item in row:
            st = st+str(item)
        print(st)
                 

def find_character(matrix, target_char):
    for row_index, row in enumerate(matrix):
        for col_index, char in enumerate(row):
            if char == target_char:
                return row_index, col_index
    return None


def itemMove(matrix,move):
    player = find_character(matrix, "$")
    box = find_character(matrix, "B")

    if move == '8':
        nextPos_x, nextPos_y = player[0]-1,player[1]
        if matrix[nextPos_x][nextPos_y] == '#':
            print('Invalid Move')
        elif matrix[nextPos_x][nextPos_y] == 'B':
            if matrix[nextPos_x-1][nextPos_y] == '#':
                print('Invalid Move')
            else:
                matrix[player[0]][player[1]] = ' '
                matrix[nextPos_x][nextPos_y] = "$"
                matrix[nextPos_x-1][nextPos_y] = "B"
        else:
            matrix[player[0]][player[1]] = ' '
            matrix[nextPos_x][nextPos_y] = "$"
    if move == '2':
        nextPos_x, nextPos_y = player[0]+1,player[1]
        if matrix[nextPos_x][nextPos_y] == '#':
            print('Invalid Move')
        elif matrix[nextPos_x][nextPos_y] == 'B':
            if matrix[nextPos_x+1][nextPos_y] == '#':
                print('Invalid Move')
            else:
                matrix[player[0]][player[1]] = ' '
                matrix[nextPos_x][nextPos_y] = "$"
                matrix[nextPos_x+1][nextPos_y] = "B"
        else:
            matrix[player[0]][player[1]] = ' '
            matrix[nextPos_x][nextPos_y] = "$"
    if move == '4':
        nextPos_x, nextPos_y = player[0],player[1]-1
        if matrix[nextPos_x][nextPos_y] == '#':
            print('Invalid Move')
        elif matrix[nextPos_x][nextPos_y] == 'B':
            if matrix[nextPos_x][nextPos_y-1] == '#':
                print('Invalid Move')
            else:
                matrix[player[0]][player[1]] = ' '
                matrix[nextPos_x][nextPos_y] = "$"
                matrix[nextPos_x][nextPos_y-1] = "B"
        else:
            matrix[player[0]][player[1]] = ' '
            matrix[nextPos_x][nextPos_y] = "$"
    if move == '6':
        nextPos_x, nextPos_y = player[0],player[1]+1
        if matrix[nextPos_x][nextPos_y] == '#':
            print('Invalid Move')
        elif matrix[nextPos_x][nextPos_y] == 'B':
            if matrix[nextPos_x][nextPos_y+1] == '#':
                print('Invalid Move')
            else:
                matrix[player[0]][player[1]] = ' '
                matrix[nextPos_x][nextPos_y] = "$"
                matrix[nextPos_x][nextPos_y+1] = "B"
        else:
            matrix[player[0]][player[1]] = ' '
            matrix[nextPos_x][nextPos_y] = "$"


matrix = readGame()
print('$ stands for player, B stands for Box, . stands for goal, # stands for obstacle')
print('8 for moving up, 2 for moving down, 4 for moving left, 6 for moving right')
while True:
    goal = find_character(matrix,'.')
    if goal == None:
        print('You win!')
        exit()
    plotCanvas(matrix)
    move = input('Enter a move: ')
    itemMove(matrix,move)
    time.sleep(0.5)
    os.system('clear')