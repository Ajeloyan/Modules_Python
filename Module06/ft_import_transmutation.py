def full_module() -> None:
    import alchemy.elements
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


def specific_func() -> None:
    from alchemy.elements import create_water
    print(f"create_water(): {create_water()}")


def aliased() -> None:
    from alchemy.potions import healing_potion as heal
    print(f"heal(): {heal()}")


def multiple() -> None:
    from alchemy.elements import create_fire, create_earth
    from alchemy.potions import strength_potion
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


def main() -> None:
    print("=== Import Transmutation Mastery ===")
    print()

    print("Method 1 - Full module import:")
    full_module()
    print()

    print("Method 2 - Specific function import:")
    specific_func()
    print()

    print("Method 3 - Aliased import:")
    aliased()
    print()

    print("Method 4 - Multiple imports:")
    multiple()
    print()

    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    main()
