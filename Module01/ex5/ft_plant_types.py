class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> None:
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming Beautifully!\n")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter} diameter")

    def produce_shade(self) -> None:
        self.shade: float = self.height * 0.5
        print(f"{self.name} provides {int(self.shade)} "
              "square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age}, days, "
              f"{self.harvest_season}\n{self.name} is rich in "
              f"{self.nutritional_value}\n")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    rose.get_info()
    rose.bloom()
    oak = Tree("Oak", 500, 1825, 50)
    oak.get_info()
    oak.produce_shade()
    Tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    Tomato.get_info()


if __name__ == "__main__":
    ft_plant_types()
