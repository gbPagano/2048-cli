from rich_menu import Menu

from src.ai_playing.montecarlo import MonteCarlo
from src.game import Game


def main() -> None:
    menu = Menu(
        "Single Player",
        "AI Playing",
        "Exit",
        rule_title="2048",
    )
    while True:
        match menu.ask():
            case "Single Player":
                Game().run()
            case "AI Playing":
                MonteCarlo().run()
            case "Exit":
                exit()


if __name__ == "__main__":
    main()
