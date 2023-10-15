from load_game import load_game
from canvas import Position, Canvas
from manual import manualMove
from solver import bfs, dfs, aStarSearch

import os
import time

canvas, box, player = load_game('./level/game3.txt')

game_mode = input('1 for bfs, 2 for dfs, 3 for manual, 4 for astar:')

if game_mode == '1':
    canvas.plot_canvas(box, player)
    # only records moves that impact boxes, pure player moves are not recorded
    beginTime = time.time()
    path = bfs(canvas, box, player)
    endTime = time.time()
    for pos, d in path:
        box.remove(pos)
        box.add(pos + d)
        canvas.plot_canvas(box, pos)
        print('The player moves to:', pos)
        print('Last move was from', pos - d,'with move of', d)
    print("Time used: ", endTime - beginTime)
    print("Pushes: ",len(path))
    exit()

if game_mode == '2':
    canvas.plot_canvas(box, player)
    # only records moves that impact boxes, pure player moves are not recorded
    beginTime = time.time()
    path = dfs(canvas, box, player)
    print(type(path))
    endTime = time.time()
    for pos, d in path:
        box.remove(pos)
        box.add(pos + d)
        canvas.plot_canvas(box, pos)
        print('The player moves to:', pos)
        print('Last move was from', pos - d,'with move of', d)
    print("Time used: ", endTime - beginTime)
    print("Pushes: ",len(path))
    exit()

if game_mode == '3':
    while True:
        canvas.plot_canvas(box, player)
        if canvas.is_finished(box):
            print('You Win!')
            exit()
        move = input('Enter a move: ')
        box, player = manualMove(canvas, player, box, move)
        time.sleep(0.5)
        os.system('clear')

if game_mode == '4':
    canvas.plot_canvas(box, player)
    # only records moves that impact boxes, pure player moves are not recorded
    beginTime = time.time()
    path = aStarSearch(canvas, box, player)
    #print(path)
    endTime = time.time()
    for pos, d in path:
        box.remove(pos)
        box.add(pos + d)
        canvas.plot_canvas(box, pos)
        print('The player moves to:', pos)
        print('Last move was from', pos - d,'with move of', d)
    print("Time used: ", endTime - beginTime)
    print("Pushes: ",len(path))
    exit()



