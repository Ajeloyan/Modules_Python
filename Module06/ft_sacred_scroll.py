import alchemy


def direct_access() -> None:
    print(f"alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")


def package_level() -> None:
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        alchemy.create_earth()
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        alchemy.create_air()
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")


def main() -> None:
    print("=== Sacred Scroll Mastery")
    print()

    print("Testing direct module access:")
    direct_access()
    print()

    print("Testing package-level access (controlled by __init__.py):")
    package_level()
    print()

    print("Package metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
