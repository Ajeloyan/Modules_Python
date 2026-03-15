class Plant:
    def __init__(self, name: str, init_height: int, age: int) -> None:
        self.name = name
        self.init_height = init_height
        self.final_height = init_height
        self.age = age

    def ages(self) -> None:
        self.age += 1

    def growths(self) -> None:
        self.final_height += 1

    def get_info(self) -> None:
        print(f"{self.name}: {self.final_height}cm, {self.age} days old")

    def simulate_week(self) -> None:
        for _ in range(6):
            self.ages()
            self.growths()


def ft_plant_growth() -> None:
    rose: Plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    rose.get_info()
    rose.simulate_week()
    print("=== Day 7 ===")
    rose.get_info()
    print(f"Growth this week : + {rose.final_height - rose.init_height}cm")


if __name__ == "__main__":
    ft_plant_growth()
