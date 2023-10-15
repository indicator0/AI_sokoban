from canvas import Position, Canvas


WALL = set(['#'])
PLAYER = set(['P', '+'])
GOAL = set(['.', '+', '*'])
BOX = set(['B', '*'])

def load_game(file):
    wall, goal, box, player = set(), set(), set(), None

    with open(file, 'r') as f:
        num_lines = int(f.readline())

        for y, line in enumerate(f.readlines()):

            if line:
                for x, char in enumerate(line):
                    #print(x,y,char)
                    pos = Position(x, y)

                    if char in WALL:
                        wall.add(pos)
                    if char in GOAL:
                        goal.add(pos)
                    if char in BOX:
                        box.add(pos)
                    if char in PLAYER:
                        player = pos
            else:
                break

    canvas = Canvas(num_lines, wall, goal)
    return canvas, box, player
