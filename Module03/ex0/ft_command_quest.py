import sys


def command_quest() -> None:
    print("=== Command Quest ===")
    n: int = len(sys.argv)

    if n <= 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {n - 1}")
        for i in range(1, n):
            print(f"Argument {i}: {sys.argv[i]}")

    print(f"Total arguments: {n}")


if __name__ == "__main__":
    command_quest()
