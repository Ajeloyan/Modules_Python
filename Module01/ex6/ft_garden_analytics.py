class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.original_height = height
        self.age = age
        self.category = "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloom = ""
        self.category = "flowering"
        if self.age >= 30:
            self.bloom = "(blooming)"


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color: str,
    ) -> None:
        super().__init__(name, height, age, color)
        self.prize = 0
        self.category = "prize flowers"
        if self.height > 15:
            self.prize += 5
        if self.age > 30:
            self.prize += 5


class Garden:
    def __init__(self, gardener: str, plants_list: list[Plant]) -> None:
        self.gardener = gardener
        self.plants_list = plants_list
        self.security_flag = True

    def add_plant(self, plant: Plant) -> None:
        if plant.height < 0:
            print(
                f"Invalid operation attempted: {plant.name}'s height "
                f"{plant.height}cm [REJECTED]"
            )
            print("Security: Negative height rejected")
            self.security_flag = False
            return
        print(f"Added {plant.name} to {self.gardener}'s garden")
        self.plants_list.append(plant)

    def grow_all(self) -> None:
        print(f"{self.gardener} is helping all plants grow ...")
        for plant in self.plants_list:
            print(f"{plant.name} grew 1cm")
            plant.age += 1
            plant.height += 1
        print()

    def display_garden(self) -> None:
        print(f"=== {self.gardener}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants_list:
            if plant.category == "regular":
                print(f" - {plant.name}: {plant.height}cm")
            elif plant.category == "flowering":
                if isinstance(plant, FloweringPlant):
                    print(
                        f" - {plant.name}: {plant.height}cm, {plant.color} "
                        f"flowers {plant.bloom}"
                    )
            elif plant.category == "prize flowers":
                if isinstance(plant, PrizeFlower):
                    print(
                        f" - {plant.name}: {plant.height}, {plant.color} "
                        f"flowers {plant.bloom}, Prize points: {plant.prize}"
                    )
        print()


class GardenManager:
    def __init__(self, gardens: list[Garden]) -> None:
        self.gardens = gardens

    @staticmethod
    def intro_printer() -> None:
        print("=== Garden Management System Demo ===\n")

    @classmethod
    def garden_network(cls, names: list[str]) -> "GardenManager":
        gardens_list = []
        for name in names:
            new_garden = Garden(name, [])
            gardens_list.append(new_garden)
        return cls(gardens_list)

    class Garden_stats:
        def __init__(self, gardens: list[Garden]) -> None:
            self.total_gardens = 0
            self.regular_count = 0
            self.flowering_count = 0
            self.prize_count = 0
            self.total_growth = 0
            self.plants_added = 0
            self.height_validation = True

            self._process_all_gardens(gardens)

        def _process_all_gardens(self, gardens: list[Garden]) -> None:
            for garden in gardens:
                self.total_gardens += 1

                if not garden.security_flag:
                    self.height_validation = False

                for plant in garden.plants_list:
                    self._analyze_plant(plant)

        def _analyze_plant(self, plant: Plant) -> None:
            self.plants_added += 1

            self.total_growth += plant.height - plant.original_height

            if plant.height <= 0:
                self.height_validation = False

            if plant.category == "regular":
                self.regular_count += 1
            elif plant.category == "flowering":
                self.flowering_count += 1
            elif plant.category == "prize flowers":
                self.prize_count += 1

        def get_garden_score_info(self, garden: Garden) -> str:
            score = 0
            for plant in garden.plants_list:
                score += plant.height
                if plant.category == "prize flowers":
                    if isinstance(plant, PrizeFlower):
                        score += plant.prize
            return f"{garden.gardener}: {score}"

        def get_report(self, gardens: list[Garden]) -> None:
            scores_line = ""
            for garden in gardens:
                info = self.get_garden_score_info(garden)
                if scores_line == "":
                    scores_line = info
                else:
                    scores_line += ", " + info

            print(f"Plants added: {self.plants_added}, Total growth: "
                  f"{self.total_growth}cm")
            print(f"Plant types: {self.regular_count} regular, "
                  f"{self.flowering_count} flowering, "
                  f"{self.prize_count} prize flowers")
            print()
            print(f"Height validation test: {self.height_validation}")
            print(f"Garden scores - {scores_line}")
            print(f"Total gardens managed: {self.total_gardens}")


if __name__ == "__main__":
    GardenManager.intro_printer()

    manager = GardenManager.garden_network(["Alice", "Bob"])

    alice_g = manager.gardens[0]
    alice_g.add_plant(Plant("Oak Tree", 100, 10))
    alice_g.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    alice_g.add_plant(PrizeFlower("Sunflower", 50, 35, "yellow"))

    print()
    alice_g.grow_all()
    alice_g.display_garden()

    stats_tool = manager.Garden_stats(manager.gardens)
    stats_tool.get_report(manager.gardens)
