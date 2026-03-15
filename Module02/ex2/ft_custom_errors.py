class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant(name: str, age: int) -> None:
    if age > 10:
        raise PlantError(f"The {name} plant is wilting!")


def check_water_level(liters: int) -> None:
    if liters < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant("tomato", 15)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        check_water_level(7)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato", 15)
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water_level(7)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
