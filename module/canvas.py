# Using relative location coordinate of board. Top left is (0,0)

class SquareLocation:
    # initialize the SquareLocation class' attributes
    def __init__(self, pos_x, pos_y):
        self.x = pos_x
        self.y = pos_y

    # redefine some magic methods for possible use
    def __add__(self, pos):
        return SquareLocation(self.x + pos.x, self.y + pos.y) 
    
    def __sub__(self, pos):
        return SquareLocation(self.x - pos.x, self.y - pos.y) 
    
    def __eq__(self, pos):
        return self.x == pos.x and self.y == pos.y
    
    def __ne__(self, pos):
        return self.x != pos.x or self.y != pos.y
    
    def __hash__(self):
        return hash((self.x, self.y))

    def get_dist(self, pos):
        return abs(self.x - pos.x) + abs(self.y - pos.y)
    
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def __repr__(self):
        return "({},{})".format(self.x, self.y)

#  define the list of available movements : up, down, right, left    
dir_list = [SquareLocation(0, -1), SquareLocation(0, 1), SquareLocation(1, 0), SquareLocation(-1, 0)]

class Canvas:
    def __init__(self, num_lines, walls, goals):
        # initialize the Canvas class' attributes
        self.num_lines = num_lines
        self.walls = walls
        self.goals = goals
        self.accessible = self.goodpattern()

    # returns available and accessible SquareLocations
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
                    if new_box_pos not in self.walls.union(boxes) and new_box_pos in self.accessible:
                        availableGrid.append((new_pos, d))
                else:
                    stack.append(new_pos)

        return availableGrid, norm_pos, visited

    def is_finished(self, boxes):
        # check if the game is finished
        return len(self.goals.difference(boxes)) == 0

    def goodpattern(self):
        # identify a pattern of dead ends within a game board. 
        # It uses a simple BFS to explore the squares surrounding goals and marked the accessible square locations
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
        # draw the board of gameplay, return a string board
        board_of_squares = []
        for item in range(self.num_lines):
            board_of_squares.append([' '] * 15) # initialize board canvas

        for wall in self.walls:  
            board_of_squares[wall.y][wall.x] = '#' # walls

        for box in boxes.difference(self.goals):  # boxes not on goal square
            board_of_squares[box.y][box.x] = 'B'

        for box in self.goals.intersection(boxes):  # boxes on goal square
            board_of_squares[box.y][box.x] = '*'

        for goal in self.goals.difference(boxes):  # goal square without boxes on it
            board_of_squares[goal.y][goal.x] = '.'

        if player in self.goals:  
            board_of_squares[player.y][player.x] = '+' # player on goal square
        else:  
            board_of_squares[player.y][player.x] = 'P' # player not on goal square
        print('\n'.join([''.join(line) for line in board_of_squares]))
