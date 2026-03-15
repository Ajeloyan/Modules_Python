class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def ft_plant_factory() -> None:
    plants_infos_list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    total_plants: int = 0
    plants_list = []
    print("=== Plant Factory Output ===")
    for info in plants_infos_list:
        plant = Plant(*info)
        plants_list.append(plant)
        total_plants += 1
    for plants in plants_list:
        plants.get_info()
    print(f"\nTotal plants created : {total_plants}")


if __name__ == "__main__":
    ft_plant_factory()
