from src.ai_playing import new_ai_game
from src.menu import index_menu
from src.single_player import new_single_game


def start() -> None:
    while True:
        choice = index_menu()
        if choice == 0:
            new_single_game()
        elif choice == 1:
            new_ai_game()
        else:
            break


if __name__ == "__main__":
    start()
