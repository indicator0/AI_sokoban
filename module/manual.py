from .canvas import SquareLocation

# takes as input a canvas, player SquareLocation, box SquareLocations, and a move direction
# It attempts to move the player in the specified direction 
# The function returns the updated box SquareLocations and player SquareLocation
def manualMove(canvas, player, box, move):
    boxSet = set()
    if move == '8':
        nextPos = player + SquareLocation(0, -1)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(0, -1) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(0, -1) not in canvas.walls:
            player = player + SquareLocation(0, -1)
            for item in box:
                if player == item:
                    item = item + SquareLocation(0, -1)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + SquareLocation(0, -1)
            boxSet = box
        return boxSet, player


    if move == '2':
        nextPos = player + SquareLocation(0, 1)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(0, 1) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(0, 1) not in canvas.walls:
            player = player + SquareLocation(0, 1)
            for item in box:
                if player == item:
                    item = item + SquareLocation(0, 1)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + SquareLocation(0, 1)
            boxSet = box
        return boxSet, player
    
    if move == '4':
        nextPos = player + SquareLocation(-1, 0)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(-1, 0) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(-1, 0) not in canvas.walls:
            player = player + SquareLocation(-1, 0)
            for item in box:
                if player == item:
                    item = item + SquareLocation(-1, 0)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + SquareLocation(-1, 0)
            boxSet = box
        return boxSet, player

    if move == '6':
        nextPos = player + SquareLocation(1, 0)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(1, 0) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + SquareLocation(1, 0) not in canvas.walls:
            player = player + SquareLocation(1, 0)
            for item in box:
                if player == item:
                    item = item + SquareLocation(1, 0)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + SquareLocation(1, 0)
            boxSet = box
        return boxSet, player
    else:
        return box, player