from src.rust_montecarlo import montecarlo

from src.game import Game


class MonteCarlo(Game):
    def get_move(self) -> str:
        iterations = 10 + self.board.moves
        depth = 5 + self.board.moves // 100
        return montecarlo(self.board.board, iterations, depth)


if __name__ == "__main__":
    MonteCarlo().run()
