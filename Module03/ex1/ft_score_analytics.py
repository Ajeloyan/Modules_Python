import sys


def score_cruncher() -> None:
    print("=== Player Score Analytics ===")
    scores: list[int] = []
    n: int = len(sys.argv)
    for i in range(1, n):
        try:
            scores.append(int(sys.argv[i]))
        except ValueError:
            print(f"Wrong scores format provided ({sys.argv[i]}). "
                  f"Usage: python3 {sys.argv[0]} <score1> <score2> ...")
            return
    if not scores:
        print(f"Wrong scores provided. Usage: python3 {sys.argv[0]} "
              "<score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    score_cruncher()
