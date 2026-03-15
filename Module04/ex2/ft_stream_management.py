import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")

    arch_id = input("Input Stream active. Enter archivist ID: ")
    status = input("Input Stream active. Enter status report: ")

    print("[STANDARD] Archive status from "
          f"{arch_id}: {status}", file=sys.stdout)
    print("[ALERT] System diagnostic: "
          "Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
