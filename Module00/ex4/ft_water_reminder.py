def ft_water_reminder() -> None:
    a: int = int(input("Days since last watering: "))
    if a > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
