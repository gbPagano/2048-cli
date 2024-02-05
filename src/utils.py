import click
from rich.align import Align
from rich.layout import Layout
from rich.rule import Rule
from rich.text import Text

from src.board import Board


def get_click() -> str | None:
    match click.getchar():
        case "\r":
            return "enter"
        case "\x1b[B" | "s" | "S"| "àP":
            return "down"
        case "\x1b[A" | "w" | "W"| "àH":
            return "up"
        case "\x1b[D" | "a" | "A"| "àK":
            return "left"
        case "\x1b[C" | "d" | "D"| "àM":
            return "right"
        case "\x1b" | "q" | "Q":
            exit()
        case _:
            return None


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
