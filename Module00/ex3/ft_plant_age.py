def ft_plant_age() -> None:
    a: int = int(input("Enter plant age in days: "))
    if a > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
