# Using relative position. Top left is 0,0

class Position:
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    def __add__(self, pos):
        return Position(self.x + pos.x, self.y + pos.y) 
    
    def __eq__(self, pos):
        return self.x == pos.x and self.y == pos.y
    
    def __ne__(self, pos):
        return self.x != pos.x or self.y != pos.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __dist__(self, pos):
        return abs(self.x - pos.x) + abs(self.y - pos.y)
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)

# available directions : up, down, right, left    
dir_list = [Position(0, -1), Position(0, 1), Position(1, 0), Position(-1, 0)]

class Canvas:
    def __init__(self, num_lines, walls, goals):
        self.num_lines = num_lines
        self.walls = walls
        self.goals = goals
        self.reachable = self._deadpattern_()


    def availableGrid(self, boxes, player):
        availableGrid = []
        stack = [player]
        norm_pos = player
        visited = set()

        while stack:
            player = stack.pop(0)
            if player in visited:
                continue
            visited.add(player)

            if player.y < norm_pos.y:
                norm_pos = player
            elif player.y == norm_pos.y and player.x < norm_pos.x:
                norm_pos = player

            for d in dir_list:
                new_pos = player + d
                if new_pos in visited or new_pos in self.walls:
                    continue
                elif new_pos in boxes:
                    new_box_pos = new_pos + d # push box
                    if new_box_pos not in self.walls.union(boxes) and new_box_pos in self.reachable:
                        availableGrid.append((new_pos, d))
                else:
                    stack.append(new_pos)

        return availableGrid, norm_pos, visited

    def is_finished(self, boxes):
        return len(self.goals.difference(boxes)) == 0

    def _deadpattern_(self):
        stack = list(self.goals)
        visited = set()

        while stack:
            pos = stack.pop(0)
            visited.add(pos)

            for d in dir_list:
                new_pos = pos + d
                if any([new_pos in visited, new_pos in self.walls, new_pos + d in self.walls]):
                    continue
                else:
                    stack.append(new_pos)
        return visited


    def plot_canvas(self, boxes, player):
        str_board = []
        for item in range(self.num_lines):
            str_board.append([' '] * 15)

        for wall in self.walls:  # wall
            str_board[wall.y][wall.x] = '#'

        for box in boxes.difference(self.goals):  # box not at goal
            str_board[box.y][box.x] = 'B'

        for box in self.goals.intersection(boxes):  # box at goal
            str_board[box.y][box.x] = '*'

        for goal in self.goals.difference(boxes):  # goal without box
            str_board[goal.y][goal.x] = '.'

        if player in self.goals:  # player at goal
            str_board[player.y][player.x] = '+'
        else:  # player not at goal
            str_board[player.y][player.x] = 'P'
        print('\n'.join([''.join(line) for line in str_board]))
