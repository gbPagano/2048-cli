import click

from rich.align import Align
from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text


def new_game():
    board = new_board()

    with Live(board, auto_refresh=False, screen=True) as live:
        ...

