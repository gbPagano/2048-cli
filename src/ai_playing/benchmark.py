from time import time

from rust_montecarlo import montecarlo

from src.board import Board


def montercarlo_newgame(moves, terminable=False) -> (bool, int, int):
    board = Board()
    while True:
        if board.moves == moves:
            return True, board.score, board.moves

        iterations = 10 + board.moves
        depth = 5 + board.moves // 100

        direction_move = montecarlo(board.board, iterations, depth)
        if direction_move and board.move(direction_move):
            board.new_piece()
        elif board.verify_end():
            return terminable, board.score, board.moves


def montecarlo_single_benchmark(n, terminable):
    res = False
    while not res:
        start = time()
        res, score, moves = montercarlo_newgame(n, terminable)
        end = time()

    return end - start, score, moves


def montecarlo_benchmark(n, m, terminable):
    exec_times, scores, all_moves = 0, 0, 0
    for i in range(n):
        exec_time, score, moves = montecarlo_single_benchmark(m, terminable)
        print(
            f"{i + 1} :: Execution Time: {round(exec_time, 2)} s :: Score: {score} :: Moves: {moves}"
        )
        exec_times += exec_time
        scores += score
        all_moves += moves

    print(
        f"RESULT :: Mean Execution Time: {round(exec_times / n, 2)} s "
        f":: Mean Score: {scores // n} :: Mean Moves: {all_moves // n}"
    )


if __name__ == "__main__":
    print("Montecarlo Time Benchmark")
    montecarlo_benchmark(20, 2500, False)
    print("--------")
    print("Montecarlo Score Benchmark")
    montecarlo_benchmark(30, 50000, True)
    print("--------")
