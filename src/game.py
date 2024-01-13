from time import sleep, time

import click
from rich.live import Live

from src.board import Board
from src.utils import get_click, print_board


class Game:
    def run(self):
        self.board = Board()

        layout = print_board(self.board.board, self.board.score, self.board.moves)
        with Live(layout, auto_refresh=False, screen=True) as live:
            live.update(layout, refresh=True)
            while True:
                try:
                    direction_move = self.get_move()
                    if direction_move and self.board.move(direction_move):
                        self.board.new_piece()
                        layout = print_board(
                            self.board.board, self.board.score, self.board.moves
                        )
                    elif self.board.verify_end():
                        layout = print_board(
                            self.board.board,
                            self.board.score,
                            self.board.moves,
                            ended=True,
                        )
                        live.update(layout, refresh=True)
                        sleep(0.8)
                        live.update(layout, refresh=True)
                        click.getchar()
                        return

                    live.update(layout, refresh=True)
                except (KeyboardInterrupt, EOFError):
                    exit()

    def benchmark(self, move_limit=None):
        while True:
            start = time()
            score, moves = self._benchmark_run(move_limit)
            end = time()

            if move_limit is None or moves == move_limit:
                return end - start, score, moves

    def _benchmark_run(self, move_limit=None):
        self.board = Board()
        while True:
            if move_limit is not None and move_limit == self.board.moves:
                return self.board.score, self.board.moves
            direction_move = self.get_move()
            if direction_move and self.board.move(direction_move):
                self.board.new_piece()
            elif self.board.verify_end():
                return self.board.score, self.board.moves

    def get_move(self):
        try:
            dir = get_click()
        except (KeyboardInterrupt, EOFError):
            exit()
        if dir != "enter":
            return dir
