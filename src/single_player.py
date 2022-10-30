import click

from rich.align import Align
from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

from src.board import Board

def new_game():
    board = Board()

    group = print_board(board.board, board.score, board.moves)


    with Live(group, auto_refresh=False, screen=True) as live:
        live.update(group, refresh=True)
        while True:
            ...
            import random
            jogada = random.choice(["up", "down","right", "left"])
            # jogada = get_click()
            if jogada and board.move(jogada):
                board.new_piece()
                group = print_board(board.board, board.score, board.moves)
            elif board.verify_end():
                group = print_board(board.board, board.score, board.moves, ended=True)
                live.update(group, refresh=True)
                click.getchar()
                break
            live.update(group, refresh=True)

            

def get_click():

    match click.getchar():
        case "\x1b[B" | "s" | "S":
            return "down"
        case "\x1b[A" | "w" | "W":
            return "up"
        case "\x1b[D" | "a" | "A":
            return "left"
        case "\x1b[C" | "d" | "D":
            return "right"
        case _:
            return None



def print_board(board, score, moves, ended=False) -> Group:
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
                    menu.append(Text.assemble(("  "),(f"{piece}", color),("  │ ")))
                elif piece < 100:
                    menu.append(Text.assemble((" "),(f"{piece}", color),("  │ ")))
                elif piece < 1000:
                    menu.append(Text.assemble((" "),(f"{piece}", color),(" │ ")))
                else:
                    menu.append(Text.assemble((f"{piece}", color),(" │ ")))
            else:
                menu.append(Text(f"     │ ", end=""))
        menu.append(Text("\n"))
        if i < 3:
            menu.append(Text(" ├──────┼──────┼──────┼──────┤\n"))
        else:
            menu.append(Text(" ╰──────┴──────┴──────┴──────╯\n"))


    score_panel = Text(f"\n Moves: {moves} | Score: {score}", justify="center")

    if ended:
        score_panel.append(Text("\nYou lose! Press any key to continue", justify="center"))

    group = Group(
        Rule("2048"),
        Align(score_panel, "center"),
        Align(menu, "center"),
    )

    return group

new_game()