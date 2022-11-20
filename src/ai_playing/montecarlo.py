from time import sleep

import click
import numpy as np
from rich.live import Live

from src.board import Board
from src.utils import get_click, print_board


def new_ai_game():
    board = Board()

    layout = print_board(board.board, board.score, board.moves)
    with Live(layout, auto_refresh=False, screen=True) as live:
        live.update(layout, refresh=True)
        while True:


            x = 10 + board.moves
            y = 5

            if board.moves > 1300: y = 10


            direction_move = montecarlo(board.board, board.score, iterations=x, iterations_2=y)
            if direction_move and board.move(direction_move):
                board.new_piece()
                layout = print_board(board.board, board.score, board.moves)
            elif board.verify_end():
                layout = print_board(board.board, board.score, board.moves, ended=True)
                live.update(layout, refresh=True)
                sleep(0.8)
                live.update(layout, refresh=True)
                click.getchar()
                break

            live.update(layout, refresh=True)


def montecarlo(board, current_score, iterations=1000, iterations_2=10):
    cp_board = Board()
    directions = {"up": 0, "down": 0, "right": 0, "left": 0}

    for direction_move in directions.keys():
        cp_board.score = 0
        for _ in range(iterations):
            cp_board.board = board.copy()

            if cp_board.move(direction_move):
                cp_board.new_piece()
            else:
                break

            # while not cp_board.verify_end():
            for _ in range(iterations_2):
                random_move = np.random.choice(list(directions.keys()))
                while not cp_board.move(random_move):
                    if cp_board.verify_end():
                        break
                    random_move = np.random.choice(list(directions.keys()))
                    
                cp_board.new_piece()

            directions[direction_move] = cp_board.score

    return sorted(directions, key=directions.get)[-1]
     

if __name__ == "__main__":
    new_ai_game()