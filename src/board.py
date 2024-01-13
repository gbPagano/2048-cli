import random

import numpy as np


class Board:
    def __init__(self) -> None:
        self.new_game()

    def new_game(self) -> None:
        self.score = 0
        self.moves = 0
        self.board = np.array(
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ]
        )

        for _ in range(2):
            pos = True
            while pos:
                i, j = random.sample(range(4), 2)
                pos = self.board[i][j]

            if random.randint(1, 10) == 1:
                self.board[i][j] = 4
            else:
                self.board[i][j] = 2

    def move(self, direction: str) -> bool:
        if direction == "down":
            self.board = np.flip(self.board)
            self.board = np.rot90(self.board)
            has_moved = self._moving()
            self.board = np.rot90(self.board, 3)
            self.board = np.flip(self.board)

        elif direction == "up":
            self.board = np.rot90(self.board)
            has_moved = self._moving()
            self.board = np.rot90(self.board, 3)

        elif direction == "right":
            self.board = np.fliplr(self.board)
            has_moved = self._moving()
            self.board = np.fliplr(self.board)

        elif direction == "left":
            has_moved = self._moving()

        if has_moved:
            self.moves += 1

        return has_moved

    def new_piece(self) -> bool:
        empty_positions = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    empty_positions.append([i, j])

        if not empty_positions:
            return False

        i, j = random.choice(empty_positions)
        if random.randint(1, 10) == 10:
            self.board[i][j] = 4
        else:
            self.board[i][j] = 2

        return True

    def verify_end(self) -> bool:
        empty_positions = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    empty_positions.append([i, j])

        if empty_positions:
            return False

        for i in range(4):
            for j in range(4):
                if j + 1 < 4:
                    if self.board[i][j] == self.board[i][j + 1]:
                        return False
                if j - 1 >= 0:
                    if self.board[i][j] == self.board[i][j - 1]:
                        return False
                if i + 1 < 4:
                    if self.board[i][j] == self.board[i + 1][j]:
                        return False
                if i - 1 >= 0:
                    if self.board[i][j] == self.board[i - 1][j]:
                        return False

        return True

    def _moving(self) -> bool:
        self.has_moved = False
        self._push()
        if self._sum():
            self._push()

        return self.has_moved

    def _push(self) -> None:
        for i in range(4):
            for j in range(1, 4):
                if self.board[i][j] != 0:
                    k = j
                    while k > 0 and self.board[i][k - 1] == 0:
                        self.board[i][k - 1], self.board[i][k] = (
                            self.board[i][k],
                            0,
                        )
                        self.has_moved = True
                        k -= 1

    def _sum(self) -> bool:
        result = False
        for i in range(4):
            for j in range(1, 4):
                if self.board[i][j] != 0:
                    if self.board[i][j - 1] == self.board[i][j]:
                        self.score += self.board[i][j] * 2
                        self.board[i][j - 1], self.board[i][j] = (
                            self.board[i][j] * 2,
                            0,
                        )
                        result = True
                        self.has_moved = True
        return result
