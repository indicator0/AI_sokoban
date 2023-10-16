from module.canvas import SquareLocation, Canvas

# read a game map from a file and create a game state "canvas"
WALL = set(['#'])
PLAYER = set(['P', '+'])
GOAL = set(['.', '+', '*'])
BOX = set(['B', '*'])

def load_game(file):
    wall, goal, box, player = set(), set(), set(), None

    with open(file, 'r') as f:
        # read the first line of the file to determine the number of lines in the game level board
        num_lines = int(f.readline())
        best = int(f.readline())
        
        for y, line in enumerate(f.readlines()):

            if line:
                for x, char in enumerate(line):
                    
                    coordinate = SquareLocation(x, y)

                    if char in WALL:
                        wall.add(coordinate)
                    if char in GOAL:
                        goal.add(coordinate)
                    if char in BOX:
                        box.add(coordinate)
                    if char in PLAYER:
                        player = coordinate
            else:
                break

    canvas = Canvas(num_lines, wall, goal)
    return canvas, box, player, best
    # creates a Canvas object and returns it along with the box and player coordinates
