from load_game import load_game
from canvas import Position, Canvas
from manual import manualMove
import os
import time

canvas, box, player = load_game('./game2.txt')

while True:
    canvas.plot_canvas(box, player)
    if canvas.is_finished(box):
        print('You Win!')
        exit()
    move = input('Enter a move: ')
    box, player = manualMove(canvas, player, box, move)
    time.sleep(0.5)
    os.system('clear')



