from rich.align import Align
from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.rule import Rule
from rich.text import Text

from src.utils import get_click


def index_menu() -> int:
    index = 0
    group = gen_index_menu()

    with Live(group, auto_refresh=False, screen=True) as live:
        live.update(group, refresh=True)
        while True:
            key = get_click()
            if key == "enter":
                return index

            index = update_index(index, key, 3)
            group = gen_index_menu(index)

            live.update(group, refresh=True)


def update_index(index: int, key: str, length: int) -> int:
    if key == "down":
        index += 1
    elif key == "up":
        index -= 1

    if index > length - 1:
        index = 0
    elif index < 0:
        index = length - 1

    return index


def gen_index_menu(index: int = 0) -> Group:
    menu = Text(justify="left")

    selected = Text("> ", "bold green")
    not_selected = Text("  ")
    options = [not_selected, not_selected, not_selected]
    options[index] = selected

    menu.append(Text.assemble(options[0], "Single Player\n"))
    menu.append(Text.assemble(options[1], ("AI Playing\n", "yellow")))
    menu.append(Text.assemble(options[2], "Exit"))

    panel = Panel.fit(menu)
    group = Group(
        Rule("MENU"),
        Align(panel, "center"),
    )
    return group


if __name__ == "__main__":
    index_menu()
