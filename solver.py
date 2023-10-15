from stateset import StateSet
import numpy as np
from queue_ori import PriorityQueue
from queue_fibo import FibonacciHeap
from scipy.optimize import linear_sum_assignment

def bfs(canvas, boxes, player):

    stack = [(frozenset(boxes), player, [])]
    state_info_cache = StateSet()

    while stack:
        boxes, player, path = stack.pop(0)

        moves, norm_pos, visited = canvas.availableGrid(boxes, player)
        state_info_cache.update(boxes, norm_pos, visited)
        #print(boxes, norm_pos)
        #print(state_info_cache.cache[boxes][norm_pos])
        for new_pos, d in moves:
            new_boxes = set(boxes)
            new_boxes.remove(new_pos)
            new_boxes.add(new_pos + d)
            new_boxes = frozenset(new_boxes)

            if (new_boxes, new_pos) in state_info_cache:
                continue
            elif canvas.is_finished(new_boxes):
                return path + [(new_pos, d)]
            else:
                stack.append((new_boxes, new_pos, path + [(new_pos, d)]))

def dfs(canvas, boxes, player):
    stack = [(frozenset(boxes), player, [])]

    state_info_cache = StateSet()

    while stack:
        boxes, player, path = stack.pop(-1)
        

        moves, norm_pos, visited = canvas.availableGrid(boxes, player)
        state_info_cache.update(boxes, norm_pos, visited)
        #print(boxes, norm_pos)
        #print(state_info_cache.cache[boxes][norm_pos])
        for new_pos, d in moves:
            new_boxes = set(boxes)
            new_boxes.remove(new_pos)
            new_boxes.add(new_pos + d)
            new_boxes = frozenset(new_boxes)
            #print(type(new_boxes))

            if (new_boxes, new_pos) in state_info_cache:
                continue
            elif canvas.is_finished(new_boxes):
                return path + [(new_pos, d)]
            else:
                stack.append((new_boxes, new_pos, path + [(new_pos, d)]))

def aStarSearch(canvas, boxes, player):

    moves, norm_pos, reachable = canvas.availableGrid(boxes, player)
    #print(moves)
    openset = FibonacciHeap()
    openset.add(
        frozenset(boxes), norm_pos, reachable, moves, 0,
        heuristic(canvas.goals, boxes))

    closedset = StateSet()
    camefrom = dict()

    while not openset.is_empty:
        state_info = openset.pop()
        closedset.update(state_info['boxes'], state_info['norm_pos'],
                         state_info['reachable'])

        tentative_gscore = state_info['gscore'] + 1

        for new_pos, d in state_info['moves']:
            #print(new_pos)
            boxes = set(state_info['boxes'])
            boxes.remove(new_pos)
            boxes.add(new_pos + d)
            boxes = frozenset(boxes)

            if (boxes, new_pos) in closedset:
                continue
            elif canvas.is_finished(boxes):
                #print(boxes)
                return [(boxes, new_pos)] + reconstruct_path(
                    camefrom, (state_info['boxes'], state_info['norm_pos']))

            norm_pos = openset.look_up((boxes, new_pos))

            if norm_pos is None:
                moves, norm_pos, reachable = canvas.availableGrid(boxes, new_pos)
                # print(moves, boxes, new_pos)
                openset.add(boxes, norm_pos, reachable, moves,
                            tentative_gscore, heuristic(canvas.goals, boxes))
            elif tentative_gscore >= openset.get_gscore((boxes, norm_pos)):
                continue

            openset.decreaseKey((boxes, norm_pos), tentative_gscore)
            camefrom[(boxes, norm_pos)] = (state_info['boxes'],
                                           state_info['norm_pos'])
            

def heuristic(goals, boxes):
    goals, boxes = list(goals), list(boxes)
    assert len(goals) == len(boxes)

    dists = np.array([[b.get_dist(g) for g in goals] for b in boxes])
    row_ind, col_ind = linear_sum_assignment(dists)

    return dists[row_ind, col_ind].sum()


def reconstruct_path(cameFrom, current):
    total_path = [current]
    print(cameFrom)
    print(current)
    print("---")
    while current in cameFrom:
        current = cameFrom[current]
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
        print(sortposBox)
    tempsortposGoals = posGoals.difference(union)
    for a in tempsortposGoals:
        sortposGoals.append((a.x,a.y))
        print(sortposGoals)
    for i in range(len(sortposBox)):
        distance += (abs(sortposBox[i][0] - sortposGoals[i][0])) + (abs(sortposBox[i][1] - sortposGoals[i][1]))
    return distance
    