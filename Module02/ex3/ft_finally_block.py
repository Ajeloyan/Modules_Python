def is_valid_plant(plant: str | None) -> None:
    if plant is None:
        raise ValueError("None - invalid plant!")


def water_plants(plant_list: list[str | None]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            is_valid_plant(plant)
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: Cannot water {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
