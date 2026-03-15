def garden_operations(error_type: str) -> None:
    if (error_type == "value"):
        _ = int("bonjour")
    elif (error_type == "zero"):
        _ = 10 / 0
    elif (error_type == "file"):
        _ = open("missing.txt")
    elif (error_type == "key"):
        garden = {"tomato": "small", "oak tree": "big"}
        _ = garden["missing_plant"]


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    print("Testing FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    print("Testing KeyError...")
    try:
        garden_operations("key")
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print()

    print("Testing multiple errors together...")
    try:
        garden_operations("zero")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
