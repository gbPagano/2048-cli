from src.menu import index_menu
from src.board import Board


def start():
    choice = index_menu()
    if choice == 0:
        new_game()


def new_game():
    
    board = Board()
    print_tabuleiro(board.board)
    while True:
        jogada = get_click()
        if jogada and board.move(jogada):
            board.new_piece()
            print_tabuleiro(board.board)
        elif board.verify_end():
            print("perder palhaço")



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

def print_tabuleiro(tabuleiro):

    print(" ╭──────┬──────┬──────┬──────╮")
    for i in range(4):
        for j in range(4):
            if not tabuleiro[i][j] == 0:
                if tabuleiro[i][j] < 10:
                    if j == 0:
                        print(f" │   {tabuleiro[i][j]}  │ ", end="")
                    else:
                        print(f"  {tabuleiro[i][j]}  │ ", end="")
                elif tabuleiro[i][j] < 100:
                    if j == 0:
                        print(f" │  {tabuleiro[i][j]}  │ ", end="")
                    else:
                        print(f" {tabuleiro[i][j]}  │ ", end="")
                elif tabuleiro[i][j] < 1000:
                    if j == 0:
                        print(f" │  {tabuleiro[i][j]} │ ", end="")
                    else:
                        print(f" {tabuleiro[i][j]} │ ", end="")
                else:
                    if j == 0:
                        print(f" │ {tabuleiro[i][j]} │ ", end="")
                    else:
                        print(f"{tabuleiro[i][j]} │ ", end="")
            else:
                if j == 0:
                    print(f" │      │ ", end="")
                else:
                    print(f"     │ ", end="")
        print()
        if i == 3:
            print(" ╰──────┴──────┴──────┴──────╯")
        else:
            print(" ├──────┼──────┼──────┼──────┤")


if __name__ == "__main__":
    start()