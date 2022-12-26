pub fn rot90(mut matrix: [[i32; 4]; 4], side: &str) -> [[i32; 4]; 4] {
    let mut new = [[0; 4]; 4];

    if side == "right" {
        matrix.reverse();
    }
    for i in 0..=3 {
        for j in 0..=3 {
            new[i][j] = matrix[j][i];
        }
    }
    if side == "left" {
        new.reverse();
    }
    new
}

pub fn flip(matrix: [[i32; 4]; 4]) -> [[i32; 4]; 4] {
    let mut new = [[0; 4]; 4];

    for i in 0..=3 {
        for j in 0..=3 {
            new[i][j] = matrix[3 - i][3 - j];
        }
    }
    new
}

pub fn fliplr(mut matrix: [[i32; 4]; 4]) -> [[i32; 4]; 4] {
    for i in 0..=3 {
        matrix[i].reverse();
    }
    matrix
}
