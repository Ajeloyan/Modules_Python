def absolute() -> None:
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


def relative() -> None:
    from alchemy.transmutation.advanced import philosophers_stone, \
        elixir_of_life
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


def package() -> None:
    import alchemy.transmutation
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


def main() -> None:
    print("=== Pathway Debate Mastery ===")
    print()

    print("Testing Absolute Imports (from basic.py):")
    absolute()
    print()

    print("Testing Relative Imports (from advanced.py):")
    relative()
    print()

    print("Testing Package Access:")
    package()
    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    main()
