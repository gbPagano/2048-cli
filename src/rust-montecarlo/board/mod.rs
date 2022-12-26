mod algebrics;

use algebrics::{flip, fliplr, rot90};
use rand::{seq::SliceRandom, Rng};

pub struct Board {
    pub score: i32,
    pub moves: i32,
    pub board: [[i32; 4]; 4],
    has_moved: bool,
}

impl Board {
    pub fn new() -> Board {
        Board {
            score: 0,
            moves: 0,
            board: [[0; 4]; 4],
            has_moved: false,
        }
    }

    pub fn movement(&mut self, direction: &str) -> bool {
        let mut has_moved = false;
        if direction == "down" {
            self.board = flip(self.board);
            self.board = rot90(self.board, "left");
            has_moved = self.moving();
            self.board = rot90(self.board, "right");
            self.board = flip(self.board);
        } else if direction == "up" {
            self.board = rot90(self.board, "left");
            has_moved = self.moving();
            self.board = rot90(self.board, "right");
        } else if direction == "right" {
            self.board = fliplr(self.board);
            has_moved = self.moving();
            self.board = fliplr(self.board);
        } else if direction == "left" {
            has_moved = self.moving();
        }

        if has_moved {
            self.moves += 1
        }
        has_moved
    }

    pub fn new_piece(&mut self) -> bool {
        let mut empty_positions: Vec<[i32; 2]> = Vec::new();

        for i in 0..4 {
            for j in 0..4 {
                if self.board[i][j] == 0 {
                    empty_positions.push([i as i32, j as i32]);
                }
            }
        }
        if empty_positions.len() > 0 {
            let pos = empty_positions.choose(&mut rand::thread_rng()).unwrap();

            let i = pos[0];
            let j = pos[1];

            if rand::thread_rng().gen_range(1..=10) == 10 {
                self.board[i as usize][j as usize] = 4;
            } else {
                self.board[i as usize][j as usize] = 2;
            }
            true
        } else {
            false
        }
    }

    pub fn verify_end(&self) -> bool {
        for i in 0..4 {
            for j in 0..4 {
                if self.board[i][j] == 0 {
                    return false;
                } else if j < 3 && self.board[i][j] == self.board[i][j + 1] {
                    return false;
                } else if j > 0 && self.board[i][j] == self.board[i][j - 1] {
                    return false;
                } else if i < 3 && self.board[i][j] == self.board[i + 1][j] {
                    return false;
                } else if i > 0 && self.board[i][j] == self.board[i - 1][j] {
                    return false;
                }
            }
        }
        true
    }

    fn moving(&mut self) -> bool {
        self.has_moved = false;
        self.push();
        if self.sum() {
            self.push();
        }
        self.has_moved
    }

    fn push(&mut self) {
        for i in 0..4 {
            for j in 0..4 {
                if self.board[i][j] != 0 && j > 0 && self.board[i][j - 1] == 0 {
                    (self.board[i][j - 1], self.board[i][j]) = (self.board[i][j], 0);
                    self.has_moved = true;
                    if j > 1 && self.board[i][j - 2] == 0 {
                        (self.board[i][j - 2], self.board[i][j - 1]) = (self.board[i][j - 1], 0);
                        if j > 2 && self.board[i][j - 3] == 0 {
                            (self.board[i][j - 3], self.board[i][j - 2]) =
                                (self.board[i][j - 2], 0);
                        }
                    }
                }
            }
        }
    }

    fn sum(&mut self) -> bool {
        let mut result = false;
        for i in 0..4 {
            for j in 0..4 {
                if self.board[i][j] != 0 {
                    if j > 0 && self.board[i][j - 1] == self.board[i][j] {
                        self.score += self.board[i][j] * 2;
                        (self.board[i][j - 1], self.board[i][j]) = (self.board[i][j] * 2, 0);
                        result = true;
                        self.has_moved = true;
                    }
                }
            }
        }
        result
    }
}
