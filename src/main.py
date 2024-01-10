from rich_menu import Menu

from src.ai_playing import new_ai_game
from src.single_player import new_single_game


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
                new_single_game()
            case "AI Playing":
                new_ai_game()
            case "Exit":
                exit()


if __name__ == "__main__":
    main()
