def ft_count_harvest_recursive() -> None:
    max: int = int(input("Days until harvest : "))

    def ft_days_received(day: int, max: int) -> None:
        if day <= max:
            print(f"Day {day}")
            ft_days_received(day + 1, max)
    ft_days_received(1, max)
    print("Harvest time !")
