import numpy as np
import random

class Board:
    def __init__(self) -> None:
        self.score = 0
        self.new_board()

    def new_board(self) -> None:
        self.board = np.array([
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ])
        for _ in range(2):
            pos = True
            while pos:
                i, j = random.sample(range(4), 2)
                pos = self.board[i][j]
            
            if random.randint(1, 10) == 1:
                self.board[i][j] = 4
            else:
                self.board[i][j] = 2

    def move(self, direction):


        if direction == "down":
            if not baixo(t, pontos):
                return False
        elif direction == "up":
            if not cima(t, pontos):
                return False
        elif direction == "right":
            if not direita(t, pontos):
                return False
        elif direction == "left":
            if not esquerda(t, pontos):
                return False

        return True




