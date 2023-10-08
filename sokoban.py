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
                return (row_index, col_index)
    return None


def itemMove(matrix,move):
    player = find_character(matrix, "$")

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


def deadPattern(matrix):
    box = find_character(matrix,'B')
    goal = find_character(matrix,'.')
    # box in a corner
    if matrix[box[0]-1][box[1]] == '#' and matrix[box[0]][box[1]-1] == '#':
        return True
    elif matrix[box[0]-1][box[1]] == '#' and matrix[box[0]][box[1]+1] == '#':
        return True
    elif matrix[box[0]+1][box[1]] == '#' and matrix[box[0]][box[1]+1] == '#':
        return True
    elif matrix[box[0]+1][box[1]] == '#' and matrix[box[0]][box[1]-1] == '#':
        return True
    else:
        return False

def availableGrid(matrix, pos):
    pos_x, pos_y = pos[0], pos[1]
    gridSet = ([pos_x-1,pos_y],[pos_x+1,pos_y],[pos_x,pos_y-1],[pos_x,pos_y+1])
    availableGrid = []
    for grid in gridSet:
        if matrix[grid[0]][grid[1]] != '#':
            availableGrid.append((grid[0],grid[1],(pos_x,pos_y))) # to trace what is the previous node
    return availableGrid


"""
def locatePrevious(closed_list, item):
    for grid in closed_list:
        if item[0] == grid[0] and item[1] == grid[1]:
            print(grid)
            return locatePrevious(closed_list,grid[2])
"""

def bfs(matrix):
    frontier_list = []
    closed_list = []
    frontier_list.append(startGrid)
    goal = find_character(matrix,'.')
    notFound = True
    route = []
    while notFound:
        frontier_list2 = []
        for item in frontier_list:
            frontier_list2.append((item[0],item[1]))
        for grid in frontier_list:
            if goal in frontier_list2:
                #print(closed_list)
                closed_list.append(grid)
                notFound = False
            elif grid not in closed_list:
                newgrid = availableGrid(matrix,grid)
                for item in newgrid:
                    frontier_list.append((item[0],item[1],item[2]))
                closed_list.append(grid)
                frontier_list = frontier_list[1:]
            else:
                continue
    print(route)



matrix = readGame()
print('$ stands for player, B stands for Box, . stands for goal, # stands for obstacle')
print('8 for moving up, 2 for moving down, 4 for moving left, 6 for moving right')
#startGrid = (find_character(matrix,'B')[0],find_character(matrix,'B')[1],(None,None))
#print(availableGrid(matrix,startGrid))
#print(bfs(matrix))
deadPattern(matrix)

"""
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
"""