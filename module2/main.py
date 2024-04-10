import time
import math
from decimal import Decimal

from nqueens import Nqueens
from fib import recursive_fib, fast_fib, matrix_fib

def main():

    for i in range(1, 20):
        queens_problem = Nqueens(i)
        if i < 9:
            start_time = time.time()
            queens_problem.brute_force_find_solution()
            end_time = time.time()
            print(f"Bruteforce ({i})")
            queens_problem.print_solution()
            duration = (end_time - start_time) * 1000
            print(f"Running time: {duration} ms\n")

        start_time = time.time()
        queens_problem.backtracking_find_solution()
        end_time = time.time()
        print(f"Backtracking ({i})")
        queens_problem.print_solution()
        duration = (end_time - start_time) * 1000
        print(f"Running time: {duration} ms\n")

    formatter = "{:.6e}"
    result = ""

    for i in range(22):
        n = int(math.pow(2, i))
        start_time = time.time()
        fib = matrix_fib(n)
        result = formatter.format(Decimal(fib))
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Matrix Fibonacci({n}) = {result}")
        print(f"Running time: {duration} ms\n")
        start_time = time.time()
        fib = fast_fib(n)
        result = formatter.format(Decimal(fib))
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        print(f"Fast Fibonacci({n}) = {result}")
        print(f"Running time: {duration} ms\n")
        if n < 40:
            start_time = time.time()
            fib = recursive_fib(n)
            result = formatter.format(Decimal(fib))
            end_time = time.time()
            duration = (end_time - start_time) * 1000
            print(f"Recursive Fibonacci({n}) = {result}")
            print(f"Running time: {duration} ms\n")


if __name__ == "__main__":
    main()
