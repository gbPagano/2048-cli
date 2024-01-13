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
        self.has_moved = false;
        if direction == "down" {
            self.push_down();
            if self.sum_down() {
                self.push_down();
            }
        } else if direction == "up" {
            self.push_up();
            if self.sum_up() {
                self.push_up();
            }
        } else if direction == "right" {
            self.push_right();
            if self.sum_right() {
                self.push_right();
            }
        } else if direction == "left" {
            self.push_left();
            if self.sum_left() {
                self.push_left();
            }
        }

        if self.has_moved {
            self.moves += 1
        }
        self.has_moved
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

    fn push_left(&mut self) {
        for i in 0..4 {
            for j in 1..4 {
                if self.board[i][j] != 0 {
                    let mut k = j;
                    while k > 0 && self.board[i][k - 1] == 0 {
                        (self.board[i][k - 1], self.board[i][k]) = (self.board[i][k], 0);
                        self.has_moved = true;
                        k -= 1;
                    }
                }
            }
        }
    }

    fn push_up(&mut self) {
        for i in 1..4 {
            for j in 0..4 {
                if self.board[i][j] != 0 {
                    let mut k = i;
                    while k > 0 && self.board[k - 1][j] == 0 {
                        (self.board[k - 1][j], self.board[k][j]) = (self.board[k][j], 0);
                        self.has_moved = true;
                        k -= 1;
                    }
                }
            }
        }
    }

    fn push_right(&mut self) {
        for i in 0..4 {
            for j in (0..3).rev() {
                if self.board[i][j] != 0 {
                    let mut k = j;
                    while k < 3 && self.board[i][k + 1] == 0 {
                        (self.board[i][k + 1], self.board[i][k]) = (self.board[i][k], 0);
                        self.has_moved = true;
                        k += 1;
                    }
                }
            }
        }
    }

    fn push_down(&mut self) {
        for i in (0..3).rev() {
            for j in 0..4 {
                if self.board[i][j] != 0 {
                    let mut k = i;
                    while k < 3 && self.board[k + 1][j] == 0 {
                        (self.board[k + 1][j], self.board[k][j]) = (self.board[k][j], 0);
                        self.has_moved = true;
                        k += 1;
                    }
                }
            }
        }
    }

    fn sum_left(&mut self) -> bool {
        let mut result = false;
        for i in 0..4 {
            for j in 1..4 {
                if self.board[i][j] != 0 {
                    if self.board[i][j - 1] == self.board[i][j] {
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

    fn sum_up(&mut self) -> bool {
        let mut result = false;
        for i in 1..4 {
            for j in 0..4 {
                if self.board[i][j] != 0 {
                    if self.board[i - 1][j] == self.board[i][j] {
                        self.score += self.board[i][j] * 2;
                        (self.board[i - 1][j], self.board[i][j]) = (self.board[i][j] * 2, 0);
                        result = true;
                        self.has_moved = true;
                    }
                }
            }
        }
        result
    }

    fn sum_right(&mut self) -> bool {
        let mut result = false;
        for i in 0..4 {
            for j in (0..3).rev() {
                if self.board[i][j] != 0 {
                    if self.board[i][j + 1] == self.board[i][j] {
                        self.score += self.board[i][j] * 2;
                        (self.board[i][j + 1], self.board[i][j]) = (self.board[i][j] * 2, 0);
                        result = true;
                        self.has_moved = true;
                    }
                }
            }
        }
        result
    }

    fn sum_down(&mut self) -> bool {
        let mut result = false;
        for i in (0..3).rev() {
            for j in 0..4 {
                if self.board[i][j] != 0 {
                    if self.board[i + 1][j] == self.board[i][j] {
                        self.score += self.board[i][j] * 2;
                        (self.board[i + 1][j], self.board[i][j]) = (self.board[i][j] * 2, 0);
                        result = true;
                        self.has_moved = true;
                    }
                }
            }
        }
        result
    }
}
