from canvas import Position

def manualMove(canvas, player, box, move):
    boxSet = set()
    if move == '8':
        nextPos = player + Position(0, -1)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(0, -1) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(0, -1) not in canvas.walls:
            player = player + Position(0, -1)
            for item in box:
                if player == item:
                    item = item + Position(0, -1)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + Position(0, -1)
            boxSet = box
        return boxSet, player


    if move == '2':
        nextPos = player + Position(0, 1)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(0, 1) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(0, 1) not in canvas.walls:
            player = player + Position(0, 1)
            for item in box:
                if player == item:
                    item = item + Position(0, 1)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + Position(0, 1)
            boxSet = box
        return boxSet, player
    
    if move == '4':
        nextPos = player + Position(-1, 0)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(-1, 0) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(-1, 0) not in canvas.walls:
            player = player + Position(-1, 0)
            for item in box:
                if player == item:
                    item = item + Position(-1, 0)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + Position(-1, 0)
            boxSet = box
        return boxSet, player

    if move == '6':
        nextPos = player + Position(1, 0)
        if nextPos in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(1, 0) in canvas.walls:
            print('Invalid Move')
            boxSet = box
        elif nextPos in box and nextPos + Position(1, 0) not in canvas.walls:
            player = player + Position(1, 0)
            for item in box:
                if player == item:
                    item = item + Position(1, 0)
                    boxSet.add(item)
                else:
                    boxSet.add(item)
        else:
            player = player + Position(1, 0)
            boxSet = box
        return boxSet, player
    else:
        return box, player