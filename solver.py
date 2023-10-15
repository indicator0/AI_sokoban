from stateset import StateSet
import numpy as np
from queue_ori import PriorityQueue
from queue_fibo import FibonacciHeap

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

    availableGrid, norm_pos, visited = canvas.availableGrid(boxes, player)
    frontier = FibonacciHeap()
    score = 0
    frontier.insert(heuristic(canvas.goals, boxes), [boxes, availableGrid, norm_pos, visited, score])
    #state_info_cache = StateSet()
    visitedSet = set()
    path = []

    while not frontier.isEmpty:

        state = frontier.extract_min()
        score = score + 1

        for new_pos, d in state[-1][1]:
            boxes = set(state[-1][0])
            boxes.remove(new_pos)
            boxes.add(new_pos + d)
            boxes = frozenset(boxes)

            if (boxes, new_pos) in visitedSet:
                continue
            elif canvas.is_finished(boxes):
                return path + [(new_pos, d)]

            if state[-1] not in visitedSet:
                visitedSet.add(state[-1])
                availableGrid, norm_pos, visited = canvas.availableGrid(boxes, new_pos)
                cost = score + heuristic(canvas.goals, boxes)
                frontier.insert(cost, [boxes, availableGrid, norm_pos, visited, score])
                
            elif cost >= frontier.score_((boxes, norm_pos)):
                continue

            path = path + [(new_pos, d)]
            
def heuristic(posGoals, posBox):
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
    