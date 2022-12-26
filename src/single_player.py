from time import sleep

import click
from rich.live import Live

from src.board import Board
from src.utils import get_click, print_board


def new_single_game() -> None:
    board = Board()

    layout = print_board(board.board, board.score, board.moves)
    with Live(layout, auto_refresh=False, screen=True) as live:
        live.update(layout, refresh=True)
        while True:
            direction_move = get_click()
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


if __name__ == "__main__":
    new_single_game()
