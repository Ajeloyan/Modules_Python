def check_temperature(temp_str: str) -> int | None:
    try:
        temp_int = int(temp_str)
        if temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        elif temp_int > 40:
            print(f"Error: {temp_int}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {temp_int}°C is perfect for plants!")
            return temp_int
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
    return None


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    print("Testing temperature: 25")
    check_temperature("25")
    print()

    print("Testing temperature: abc")
    check_temperature("abc")
    print()

    print("Testing temperature: 100")
    check_temperature("100")
    print()

    print("Testing temperature: -50")
    check_temperature("-50")
    print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
