from typing import Generator
import time


def fibonacci_gen() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_gen() -> Generator[int, None, None]:
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def ft_event_generator(n: int) -> Generator[tuple, None, None]:
    levels = {"alice": 5, "bob": 12, "charlie": 8}
    players = ["alice", "bob", "charlie"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(1, n + 1):
        p_idx = i % 3
        a_idx = (i + (i // 3)) % 3

        p_name = players[p_idx]
        action = actions[a_idx]

        if action == "leveled up":
            levels[p_name] += 1

        curr_lvl = levels[p_name]
        msg = f"Event {i}: Player {p_name} (level {curr_lvl}) {action}"
        yield (msg, curr_lvl)


if __name__ == "__main__":
    game = ft_event_generator(1000)

    total_ev = 0
    high_lvl = 0
    treasures = 0
    level_ups = 0

    start = time.time()
    for event, level in game:
        total_ev += 1

        if total_ev <= 3:
            print(event)
        elif total_ev == 4:
            print("...")

        if level >= 10:
            high_lvl += 1
        if "found treasure" in event:
            treasures += 1
        elif "leveled up" in event:
            level_ups += 1
    end = time.time()
    print()

    print("=== Stream Analytics ===")

    print(f"Total events processed: {total_ev}")
    print(f"High-level players (10+): {high_lvl}")
    print(f"Treasure events: {treasures}")
    print(f"Level-up events: {level_ups}")
    print()
    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {end - start:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fib = fibonacci_gen()
    print("Fibonacci sequence (first 10): ", end="")
    for i in range(10):
        print(next(fib), end="")
        if i < 9:
            print(", ", end="")
        else:
            print()
    prime = prime_gen()
    print("Prime numbers (first 5): ", end="")
    for i in range(5):
        print(next(prime), end="")
        if i < 4:
            print(", ", end="")
        else:
            print()
