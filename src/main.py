from src.menu import index_menu



def start():
    choice = index_menu()
    if choice == 0:
        new_game()


def new_game():
    ...


if __name__ == "__main__":
    start()