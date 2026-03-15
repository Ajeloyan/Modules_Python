class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants: list[str] = []

    def add_plant(self, name: str) -> None:
        if name == "":
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(name)
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        if not self.plants:
            return

        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name: str, water: int, sun: int) -> str:
        if water < 1 or water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if sun < 2 or sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        return f"{name}: healthy (water: {water}, sun: {sun})"

    def check_tank_status(self, water_liters: int) -> None:
        if water_liters < 10:
            raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    manager = GardenManager()
    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except ValueError as e:
        print(f"Error adding plant: {e}")
    print()

    print("Watering plants...")
    manager.water_plants()
    print()

    print("Checking plant health...")
    try:
        print(manager.check_plant_health("tomato", 5, 8))
        print(manager.check_plant_health("lettuce", 15, 8))
    except PlantError as e:
        print(f"Error checking lettuce: {e}")
    print()

    print("Testing error recovery...")
    try:
        manager.check_tank_status(5)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
