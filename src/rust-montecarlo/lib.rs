mod board;

use board::Board;
use pyo3::prelude::*;
use rand::prelude::SliceRandom;
use rayon::prelude::*;
use std::collections::HashMap;
use std::sync::mpsc::channel;

/// A Python module implemented in Rust.
#[pymodule]
fn rust_montecarlo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(montecarlo, m)?)?;
    Ok(())
}

#[pyfunction]
fn montecarlo(board: [[i32; 4]; 4], iterations: i32, depth: i32) -> PyResult<String> {
    let mut results = HashMap::from([("up", 0), ("down", 0), ("right", 0), ("left", 0)]);
    let directions = ["up", "down", "right", "left"];

    for (key, value) in results.iter_mut() {
        let (sender, receiver) = channel();
        (0..iterations)
            .into_par_iter()
            .for_each_with(sender, |s, _| {
                let mut cp_board = Board::new();
                cp_board.score = 0;
                cp_board.board = board;
                if cp_board.movement(key) {
                    cp_board.new_piece();
                } else {
                    return;
                }
                for _ in 0..depth {
                    while !cp_board.movement(directions.choose(&mut rand::thread_rng()).unwrap()) {
                        if cp_board.verify_end() {
                            return;
                        }
                    }
                    cp_board.new_piece();
                }
                s.send(cp_board.score).unwrap();
            });
        *value = receiver.iter().sum();
    }
    let best = results.iter().max_by_key(|entry| entry.1).unwrap();
    Ok(best.0.to_string())
}
