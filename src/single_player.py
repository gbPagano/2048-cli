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

    group = print_board(board.board)


    with Live(group, auto_refresh=False, screen=True) as live:
        live.update(group, refresh=True)
        while True:
            ...
            import random
            jogada = random.choice(["up", "down","right", "left"])
            jogada = get_click()
            if jogada and board.move(jogada):
                board.new_piece()
                group = print_board(board.board)
            elif board.verify_end():
                print("perdeu palhaço")
                input()
                break

            live.update(group, refresh=True)
            

def get_click():
    import click
    key = click.getchar()

    if key in ("\x1b[B", "s", "S"):
        return "down"
    elif key in ("\x1b[A", "w", "W"):
        return "up"
    elif key in ("\x1b[D", "a", "A"):
        return "left"
    elif key in ("\x1b[C", "d", "D"):
        return "right"
    else:
        return None

def print_board(board) -> Group:
    menu = Text(justify="left")

    menu.append(Text(" ╭──────┬──────┬──────┬──────╮\n"))
    for i in range(4):
        for j in range(4):
            if not board[i][j] == 0:
                if board[i][j] < 10:
                    if j == 0:
                        menu.append(Text(f" │   {board[i][j]}  │ ", end=""))
                    else:
                        menu.append(Text(f"  {board[i][j]}  │ ", end=""))
                elif board[i][j] < 100:
                    if j == 0:
                        menu.append(Text(f" │  {board[i][j]}  │ ", end=""))
                    else:
                        menu.append(Text(f" {board[i][j]}  │ ", end=""))
                elif board[i][j] < 1000:
                    if j == 0:
                        menu.append(Text(f" │  {board[i][j]} │ ", end=""))
                    else:
                        menu.append(Text(f" {board[i][j]} │ ", end=""))
                else:
                    if j == 0:
                        menu.append(Text(f" │ {board[i][j]} │ ", end=""))
                    else:
                        menu.append(Text(f"{board[i][j]} │ ", end=""))
            else:
                if j == 0:
                    menu.append(Text(f" │      │ ", end=""))
                else:
                    menu.append(Text(f"     │ ", end=""))
        menu.append(Text('\n'))
        if i == 3:
            menu.append(Text(" ╰──────┴──────┴──────┴──────╯\n"))
        else:
            menu.append(Text(" ├──────┼──────┼──────┼──────┤\n"))


    panel = Panel.fit(menu)

    group = Group(
        Rule("2048"),
        Align(menu, "center"),
    )
    return group

new_game()