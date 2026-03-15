class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        print(f"Plant created: {name}")
        self.__age = age
        self.__height = height
        self.__name = name

    def get_age(self) -> int:
        return self.__age

    def get_height(self) -> int:
        return self.__height

    def get_name(self) -> str:
        return self.__name

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = height
            print(f"Height updated: {self.__height} cm [OK]")


def ft_garden_security() -> None:
    print("=== Garden security system ===")
    rose = Plant("Rose", 0, 0)
    rose.set_height(25)
    rose.set_age(30)
    print()
    rose.set_height(-5)
    print((f"Current plant: {rose.get_name()} ({rose.get_height()}cm, "
           f"{rose.get_age()} days)"))


if __name__ == "__main__":
    ft_garden_security()
