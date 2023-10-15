from load_game import load_game
from canvas import Position, Canvas
from manual import manualMove
from solver import bfs, dfs, aStarSearch

import os
import time
import seaborn as sns
import matplotlib.pyplot as plt
from canvas import Canvas

def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname


canvas, box, player = load_game('./level/game3.txt')

game_mode = input('1 for bfs, 2 for dfs, 3 for manual, 4 for astar, 5 for benchmark:')

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
    #print(type(path))
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
    print(path[::-1])
    endTime = time.time()
    for boxes, player in path[::-1]:
        canvas.plot_canvas(boxes, player)
    # for pos, d in path:
    #     box.remove(pos)
    #     box.add(pos + d)
    #     canvas.plot_canvas(box, pos)
    #     print('The player moves to:', pos)
    #     print('Last move was from', pos - d,'with move of', d)
    # print("Time used: ", endTime - beginTime)
    print("Pushes: ",len(path))
    exit()

if game_mode == '5':
    # Benchmark performance with some gameplays
    base = './benchmark/'
    push_bfs = push_dfs = push_astar = 0
    for i in findAllFile(base):
        canvas, box, player = load_game(i)
        path_bfs = bfs(canvas, box, player)
        push_bfs = push_bfs + len(path_bfs)
        path_dfs = dfs(canvas, box, player)
        push_dfs = push_dfs + len(path_dfs)
        path_astar = aStarSearch(canvas, box, player)
        push_astar = push_astar + len(path_astar)
        print(push_bfs , push_dfs , push_astar)
    x = ['BFS', 'DFS', 'A*']
    y = [push_bfs, push_dfs, push_astar]
    dic = dict(zip(x, y))
    
    print(f"Total Pushes with BFS: {push_bfs} \n")
    print(f"Total Pushes with DFS: {push_dfs} \n")
    print(f"Total Pushes with A*: {push_astar} \n")

    sns.set_style("dark")
    ax = sns.barplot(x=list(dic.keys()),y=list(dic.values()))
    ax.set_title('Benchmark')
    ax.bar_label(ax.containers[0])
    plt.savefig("plot.png", dpi=300)
    exit()


