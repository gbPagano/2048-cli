from time import sleep

import click
from rich.align import Align
from rich.layout import Layout
from rich.live import Live
from rich.rule import Rule
from rich.text import Text

from src.board import Board
from src.utils import get_click


def new_single_game() -> None:
    board = Board()

    layout = print_board(board.board, board.score, board.moves)

    with Live(layout, auto_refresh=False, screen=True) as live:
        live.update(layout, refresh=True)
        while True:

            import random  # retirar

            jogada = random.choice(["up", "down", "right", "left"])  # retirar
            jogada = get_click()
            if jogada and board.move(jogada):
                board.new_piece()
                layout = print_board(board.board, board.score, board.moves)
            elif board.verify_end():
                layout = print_board(board.board, board.score, board.moves, ended=True)
                live.update(layout, refresh=True)
                sleep(0.5)
                click.getchar()
                break

            live.update(layout, refresh=True)


def print_board(board: Board, score: int, moves: int, ended=False) -> Layout:
    menu = Text()
    menu.append(Text(" ╭──────┬──────┬──────┬──────╮\n"))
    for i in range(4):
        for j in range(4):
            piece = board[i][j]

            match piece:
                case 2 | 4:
                    color = ""
                case 8 | 16:
                    color = "bright_yellow"
                case 32 | 64:
                    color = "orange1"
                case 128 | 256:
                    color = "dark_orange"
                case 512 | 1024:
                    color = "orange_red1"
                case 2048:
                    color = "red"
                case _:
                    color = "dark_red"

            if j == 0:
                menu.append(Text(f" │ ", end=""))
            if piece:
                if piece < 10:
                    menu.append(Text.assemble(("  "), (f"{piece}", color), ("  │ ")))
                elif piece < 100:
                    menu.append(Text.assemble((" "), (f"{piece}", color), ("  │ ")))
                elif piece < 1000:
                    menu.append(Text.assemble((" "), (f"{piece}", color), (" │ ")))
                else:
                    menu.append(Text.assemble((f"{piece}", color), (" │ ")))
            else:
                menu.append(Text(f"     │ ", end=""))
        menu.append(Text("\n"))
        if i < 3:
            menu.append(Text(" ├──────┼──────┼──────┼──────┤\n"))
        else:
            menu.append(Text(" ╰──────┴──────┴──────┴──────╯\n"))

    layout = Layout()
    layout.split_column(
        Layout(Rule("2048"), size=1),
        Layout(name="score", size=2),
        Layout(Align(menu, "center"), size=9),
    )
    layout["score"].split_row(
        Layout(Text(f"\nMoves: {moves}", justify="right")),
        Layout(Text("\n|", justify="center"), size=3),
        Layout(Text(f"\nScore: {score}", justify="left")),
    )
    if ended:
        layout.add_split(
            Layout(Text("You lose! Press any key to continue", justify="center")),
        )

    return layout


if __name__ == "__main__":
    new_single_game()
