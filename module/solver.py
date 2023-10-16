from .stateset import StateSet
import numpy as np
from .PriorityQueue import FibonacciHeap
from scipy.optimize import linear_sum_assignment

# This function mimics the pushing move, simulaiting pushing all nearby boxes to directions accordingly.
def generateNewBoundary(currBoxSet, availablegrid, nextmove):
    currBoxSet.remove(availablegrid) # eliminate box at current position
    currBoxSet.add(availablegrid + nextmove) # push to a new place
    return frozenset(currBoxSet)

def bfs(canvas, boxes, player):

    grid_list = [(frozenset(boxes), player, [])] # initializing grid_list and defining the data structure of grid. The last element is recorded path.
    info_of_state = StateSet() # initializing a StateSet to store visited status.

    while True:
        boxes, player, path = grid_list.pop(0) # pop the first element in grid_list

        moves, norm_pos, accessible = canvas.availableGrid(boxes, player) # generate available grids and moves for current boxes positions and player's position
        info_of_state.update(boxes, norm_pos, accessible) # update visited status set

        for new_square, change in moves:
            new_boxes = set(boxes)
            new_boxes = generateNewBoundary(new_boxes, new_square, change) # generate a new discovering boundary with one box being moved.

            if canvas.is_finished(new_boxes):
            # if game is done, return the path
                return path + [(new_square, change)] 
            if (new_boxes, new_square) in info_of_state:
                continue # if a status is visited, for example, moving from (2,2) to (2,2+1) with move (0,1) and boxes are in postion xxx, then we update nothing.
            else:
                grid_list.append((new_boxes, new_square, path + [(new_square, change)] )) # update our list of grids/status to be visited

def dfs(canvas, boxes, player): # almost the same as bfs, but this time we pop the last element in grid_list to conduct a depth first searching.
    grid_list = [(frozenset(boxes), player, [])]

    info_of_state = StateSet()

    while True:
        boxes, player, path = grid_list.pop(-1)

        moves, norm_pos, accessible = canvas.availableGrid(boxes, player)
        info_of_state.update(boxes, norm_pos, accessible)
        #print(boxes, norm_pos)
        #print(info_of_state.cache[boxes][norm_pos])
        for new_square, change in moves:
            new_boxes = set(boxes)
            new_boxes = generateNewBoundary(new_boxes, new_square, change)
            #print(type(new_boxes))

            if canvas.is_finished(new_boxes):
                return path + [(new_square, change)] 
            if (new_boxes, new_square) in info_of_state:
                continue
            else:
                grid_list.append((new_boxes, new_square, path + [(new_square, change)] ))

def aStarSearch(canvas, boxes, player):

    # implement A* algorithm, return a list of recorded path
    open_list = FibonacciHeap()
    closed_list = StateSet()
    recorded_path = dict()

    moves, norm_pos, accessible = canvas.availableGrid(boxes, player) # generate available grids and moves for current boxes positions and player's position

    init_f = 0
    open_list.add(frozenset(boxes), norm_pos, accessible, moves, init_f, heuristic(canvas.goals, boxes)) # initialize the open_list with a starting status

    while not open_list.is_empty:
        state_info = open_list.pop() # pop the first element in open_list (as a fibonacci heap)
        closed_list.update(state_info['boxes'], state_info['norm_pos'], state_info['accessible']) # update visited status

        for new_square, change in state_info['moves']:
            # before searching, we protect the real boxes and create an imagined environment to "move" boxes
            new_boxes = set(state_info['boxes'])
            boxes = generateNewBoundary(new_boxes, new_square, change) # same as dfs and bfs.

            if canvas.is_finished(boxes):
                return [(boxes, new_square)] + generate_path(recorded_path, (state_info['boxes'], state_info['norm_pos']))
            if (boxes, new_square) in closed_list:
                continue

            norm_pos = open_list.find((boxes, new_square)) # look up if this status (with these boxes position and player position) is visited.
            #If so, we should get a norm_pos, then we go to the elif; If not, we get nothing returned, and we add this status into the open_list to discover.
            total_distance_cost = state_info['gscore'] + 1 # total distance = current gscore + 1 move length
            
            if norm_pos is None:
                moves, norm_pos, accessible = canvas.availableGrid(boxes, new_square)
                open_list.add(boxes, norm_pos, accessible, moves, total_distance_cost, heuristic(canvas.goals, boxes))
            elif total_distance_cost >= open_list.get_gscore((boxes, norm_pos)): # we don't update the open list if proposed move is not better than current one
                continue
            
            # reorder with a descent order w.r.t f_score.
            open_list.decreaseKey((boxes, norm_pos), total_distance_cost)
            recorded_path[(boxes, norm_pos)] = (state_info['boxes'], state_info['norm_pos'])
    print('Failed to find a path with A star.')
    return None
            

def heuristic(goals, boxes):
    goals, boxes = list(goals), list(boxes)
    all_distances = np.array([[box.get_dist(gol) for gol in goals] for box in boxes])
    index_row, index_col = linear_sum_assignment(all_distances)

    return sum(all_distances[index_row, index_col])


def generate_path(recorded_path, current):
    total_path = [current]
    while current in recorded_path:
        current = recorded_path[current]
        total_path.append(current)
    return total_path

# Deprecated version of heuristic
def heuristicORG(posGoals, posBox):
    distance = 0
    sortposBox = []
    sortposGoals = []
    union = posGoals & posBox
    tempsortposBox = posBox.difference(union)
    for a in tempsortposBox:
        sortposBox.append((a.x,a.y))
    tempsortposGoals = posGoals.difference(union)
    for a in tempsortposGoals:
        sortposGoals.append((a.x,a.y))
    for i in range(len(sortposBox)):
        distance += (abs(sortposBox[i][0] - sortposGoals[i][0])) + (abs(sortposBox[i][1] - sortposGoals[i][1]))
    return distance
    