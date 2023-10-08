from stateset import StateSet

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

            if (new_boxes, new_pos) in state_info_cache:
                continue
            elif canvas.is_finished(new_boxes):
                return path + [(new_pos, d)]
            else:
                stack.append((new_boxes, new_pos, path + [(new_pos, d)]))