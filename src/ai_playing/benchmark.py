from src.ai_playing.montecarlo import MonteCarlo


def montecarlo_benchmark(n, move_limit=None):
    exec_times, scores, all_moves = 0, 0, 0
    for i in range(n):
        exec_time, score, moves = MonteCarlo().benchmark(move_limit)
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
    montecarlo_benchmark(20, 2500)
    print("--------")
    print("Montecarlo Score Benchmark")
    montecarlo_benchmark(30)
    print("--------")
