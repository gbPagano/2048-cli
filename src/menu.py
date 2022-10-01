import click

from rich.align import Align
from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text


def index_menu() -> int:
    index = 0
    group = gen_index_menu()

    with Live(group, auto_refresh=False, screen=True) as live:
        live.update(group, refresh=True)
        while True:
            key = click.getchar()

            if key == "\r":
                return index
            elif key in ("\x1b", "q", "Q"):
                return -1

            index = get_index_choice(index, key, 2)
            group = gen_index_menu(index)

            live.update(group, refresh=True)


def get_index_choice(index: int , key: str, length: int) -> int:
    if key in ("\x1b[B", "s", "S"):
        index += 1
    elif key in ("\x1b[A", "w", "W"):
        index -= 1

    if index > length - 1:
        index = 0
    elif index < 0:
        index = length - 1

    return index


def gen_index_menu(index: int = 0) -> Group:
    menu = Text(justify="left")

    selected = Text("> ")
    selected.stylize("bold green",0, 1)
    not_selected = Text("  ")
    options = [not_selected, not_selected]
    options[index] = selected

    linha_1 = options[0] + Text("Single Player\n")
    linha_2 = options[1] + Text("AI Playing")
    menu.append(linha_1)
    menu.append(linha_2)
    panel = Panel.fit(menu)

    group = Group(
        Rule("MENU"),
        Align(panel, "center"),
    )
    return group


if __name__ == "__main__":
    index_menu()
