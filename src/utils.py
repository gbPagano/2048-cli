import click


def get_click() -> str | None:
    match click.getchar():
        case "\r":
            return "enter"
        case "\x1b[B" | "s" | "S":
            return "down"
        case "\x1b[A" | "w" | "W":
            return "up"
        case "\x1b[D" | "a" | "A":
            return "left"
        case "\x1b[C" | "d" | "D":
            return "right"
        case "\x1b" | "q" | "Q":
            exit()
        case _:
            return None