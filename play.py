from load_game import load_game
from module.manual import manualMove
from module.solver import bfs, dfs, aStarSearch
#from module.canvas import SquareLocation, Canvas
import os
import time
import seaborn as sns
import matplotlib.pyplot as plt

# read all the test cases in the benchmark folder
def findAllFile(base):
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

# load game level board
canvas, box, player, best = load_game('./benchmark/case5.txt')

# choose game mode
game_mode = input('Enter 1 for manual, 2 for bfs, 3 for dfs, 4 for astar, 5 for benchmark:\n')

# manual gameplay
if game_mode == '1':
    while True:
        canvas.plot_canvas(box, player)
        if canvas.is_finished(box):
            print('You Win!')
            exit()
        move = input('Enter a move: ')
        box, player = manualMove(canvas, player, box, move)
        time.sleep(0.5)
        os.system('clear')

# auto gameplay with breath first search algorithm
if game_mode == '2':
    canvas.plot_canvas(box, player)
    # only records moves that impact boxes, pure player moves are not recorded
    beginTime = time.time()
    path = bfs(canvas, box, player)
    endTime = time.time()
    #print(type(path))
    #print(path)
    for pos, d in path:
        box.remove(pos)
        box.add(pos + d)
        canvas.plot_canvas(box, pos)
        print('The player moves to:', pos)
        print('Last move was from', pos - d,'with move of', d)
    print("Time used: ", endTime - beginTime)
    print("Pushes: ",len(path))
    exit()

# auto gameplay with depth first search algorithm
if game_mode == '3':
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

# auto gameplay with a-star(a*) algorithm
if game_mode == '4':
    canvas.plot_canvas(box, player)
    # only records moves that impact boxes, pure player moves are not recorded
    beginTime = time.time()
    path = aStarSearch(canvas, box, player)
    path = path[::-1]

    for i in range(len(path) - 1):
        old_box_pos = path[i][0]
        new_box_pos = path[i+1][0]
        difference_order_first = [x for x in old_box_pos if x not in new_box_pos]
        difference_order_second = [y for y in new_box_pos if y not in old_box_pos]
        d = difference_order_second[0] - difference_order_first[0]
        pos = difference_order_first[0]
        box.remove(pos)
        box.add(pos + d)
        canvas.plot_canvas(box, pos)
        print('The player moves to:', pos)
        print('Last move was from', pos - d,'with move of', d)
        
    endTime = time.time()
    print("Time used: ", endTime - beginTime)
    print("Pushes: ",len(path))
    exit()

# Run benchmark performance evaluation with test cases
# Measured by push and time
if game_mode == '5':
    
    print("Running benchmark...")
    base = './benchmark/'
    push_bfs = push_dfs = push_astar = push_best = 0
    bfs_time = dfs_time = astar_time = 0
        
    for i in findAllFile(base):
        canvas, box, player, best = load_game(i)

        push_best = push_best + best

        beginTime = time.time()
        path_bfs = bfs(canvas, box, player)
        push_bfs = push_bfs + len(path_bfs)
        endTime = time.time()
        usedTime = endTime - beginTime
        bfs_time = bfs_time + usedTime

        beginTime = time.time()
        path_dfs = dfs(canvas, box, player)
        push_dfs = push_dfs + len(path_dfs)
        endTime = time.time()
        usedTime = endTime - beginTime   
        dfs_time = dfs_time + usedTime     

        beginTime = time.time()
        path_astar = aStarSearch(canvas, box, player)
        push_astar = push_astar + len(path_astar)
        endTime = time.time()
        usedTime = endTime - beginTime
        astar_time = astar_time + usedTime
    
    x_push = ['BFS', 'DFS', 'A*', 'Best human']
    x_time = ['BFS', 'DFS', 'A*']
    y_push = [push_bfs, push_dfs, push_astar, push_best]
    y_time = [bfs_time, dfs_time, astar_time]
    dic_push = dict(zip(x_push, y_push))
    dic_time = dict(zip(x_time, y_time))
    
    print(f"BFS : Total Pushes: {push_bfs} | Time used: {bfs_time} s")
    print(f"DFS : Total Pushes: {push_dfs} | Time used: {dfs_time} s")
    print(f"A* : Total Pushes: {push_astar} | Time used: {astar_time} s")
    print(f"Best Human Pushes Record: {push_best} ")

    sns.set_style("dark")
    ax_1 = sns.barplot(x=list(dic_push.keys()),y=list(dic_push.values()))
    ax_1.set_title('Benchmark by Push')
    ax_1.bar_label(ax_1.containers[0])
    plt.savefig("plot_PUSH.png", dpi=300)
    plt.close()
    ax_2 = sns.barplot(x=list(dic_time.keys()),y=list(dic_time.values()))
    ax_2.set_title('Benchmark by Time')
    ax_2.bar_label(ax_2.containers[0])
    plt.savefig("plot_TIME.png", dpi=300)
    plt.close()
    exit()


