from stateset import StateSet
import numpy as np
from queue_fibo import FibonacciHeap
from scipy.optimize import linear_sum_assignment

def bfs(canvas, boxes, player):

    stack = [(frozenset(boxes), player, [])]
    info_of_state = StateSet()

    while stack:
        boxes, player, path = stack.pop(0)

        moves, norm_pos, visited = canvas.availableGrid(boxes, player)
        info_of_state.update(boxes, norm_pos, visited)
        #print(boxes, norm_pos)
        #print(info_of_state.cache[boxes][norm_pos])
        for new_square, change in moves:
            new_boxes = set(boxes)
            new_boxes.remove(new_square)
            new_boxes.add(new_square + change)
            new_boxes = frozenset(new_boxes)

            if (new_boxes, new_square) in info_of_state:
                continue
            elif canvas.is_finished(new_boxes):
                return path + [(new_square, change)]
            else:
                stack.append((new_boxes, new_square, path + [(new_square, change)]))

def dfs(canvas, boxes, player):
    stack = [(frozenset(boxes), player, [])]

    info_of_state = StateSet()

    while stack:
        boxes, player, path = stack.pop(-1)
        

        moves, norm_pos, visited = canvas.availableGrid(boxes, player)
        info_of_state.update(boxes, norm_pos, visited)
        #print(boxes, norm_pos)
        #print(info_of_state.cache[boxes][norm_pos])
        for new_square, change in moves:
            new_boxes = set(boxes)
            new_boxes.remove(new_square)
            new_boxes.add(new_square + change)
            new_boxes = frozenset(new_boxes)
            #print(type(new_boxes))

            if (new_boxes, new_square) in info_of_state:
                continue
            elif canvas.is_finished(new_boxes):
                return path + [(new_square, change)]
            else:
                stack.append((new_boxes, new_square, path + [(new_square, change)]))

def aStarSearch(canvas, boxes, player):

    # implement A* algorithm, return a list of recorded path
    moves, norm_pos, accessible = canvas.availableGrid(boxes, player)
    init_cost = 0
    open_list = FibonacciHeap()
    open_list.add(frozenset(boxes), norm_pos, accessible, moves, init_cost, heuristic(canvas.goals, boxes))

    closed_list = StateSet()
    recorded_path = dict()

    while not open_list.is_empty:
        state_info = open_list.pop()
        closed_list.update(state_info['boxes'], state_info['norm_pos'],
                         state_info['accessible'])

        total_distance_cost = state_info['gscore'] + 1

        for new_square, change in state_info['moves']:
            #print(new_square)
            boxes = set(state_info['boxes'])
            boxes.remove(new_square)
            boxes.add(new_square + change)
            boxes = frozenset(boxes)

            if (boxes, new_square) in closed_list:
                continue
            elif canvas.is_finished(boxes):
                #print(boxes)
                return [(boxes, new_square)] + generate_path(
                    recorded_path, (state_info['boxes'], state_info['norm_pos']))

            norm_pos = open_list.find((boxes, new_square))

            if norm_pos is None:
                moves, norm_pos, accessible = canvas.availableGrid(boxes, new_square)
                # print(moves, boxes, new_square)
                open_list.add(boxes, norm_pos, accessible, moves,
                            total_distance_cost, heuristic(canvas.goals, boxes))
            elif total_distance_cost >= open_list.get_gscore((boxes, norm_pos)):
                continue

            open_list.decreaseKey((boxes, norm_pos), total_distance_cost)
            recorded_path[(boxes, norm_pos)] = (state_info['boxes'],
                                           state_info['norm_pos'])
            

def heuristic(goals, boxes):
    goals, boxes = list(goals), list(boxes)
    all_distances = np.array([[b.get_dist(g) for g in goals] for b in boxes])
    row_ind, col_ind = linear_sum_assignment(all_distances)

    return all_distances[row_ind, col_ind].sum()


def generate_path(recorded_path, current):
    total_path = [current]
    while current in recorded_path:
        current = recorded_path[current]
        total_path.append(current)
    return total_path

def heuristic2(posGoals, posBox):
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
    