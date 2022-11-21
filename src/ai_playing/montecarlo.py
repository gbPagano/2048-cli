from multiprocessing import Pool
from os import cpu_count
from time import sleep

import click
import numpy as np
from rich.live import Live

from src.board import Board
from src.utils import make_processes_pool, print_board


def new_ai_game() -> None:
    pool = make_processes_pool()
    board = Board()

    layout = print_board(board.board, board.score, board.moves)
    with Live(layout, auto_refresh=False, screen=True) as live:
        live.update(layout, refresh=True)
        while True:
            iterations = 10 + board.moves
            depth = 5

            if board.moves > 990:   
                iterations = 1000
                depth = 10

            direction_move = multiprocess_montecarlo(
                board.board, pool, iterations=iterations, depth=depth
            )
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


def montecarlo(board: Board, iterations: int, depth: int) -> dict:
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
            for _ in range(depth):
                random_move = np.random.choice(list(directions.keys()))
                while not cp_board.move(random_move):
                    if cp_board.verify_end():
                        break
                    random_move = np.random.choice(list(directions.keys()))

                cp_board.new_piece()

        directions[direction_move] = cp_board.score

    return directions


def multiprocess_montecarlo(board: Board, pool: Pool, iterations=1000, depth=10) -> str:
    directions = {"up": 0, "down": 0, "right": 0, "left": 0}

    variaveis = [[board, iterations // cpu_count(), depth]] * cpu_count()
    results = pool.starmap(montecarlo, variaveis)
    for dic in results:
        for key in dic:
            directions[key] += dic[key]

    return sorted(directions, key=directions.get)[-1]


if __name__ == "__main__":
    new_ai_game()
