import math


def calculate_distance(
    coord1: tuple[int, int, int],
    coord2: tuple[int, int, int]
) -> float:
    (x1, y1, z1) = coord1
    (x2, y2, z2) = coord2

    distance: float = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return (distance)


def parse_coordinates(coord_str: str) -> tuple[int, int, int] | None:
    try:
        parts: list[str] = coord_str.split(',')
        return (int(parts[0]), int(parts[1]), int(parts[2]))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None


def coordinate_system() -> None:
    print("=== Game Coordinate System ===\n")

    origin: tuple[int, int, int] = (0, 0, 0)
    end: tuple[int, int, int] = (10, 20, 5)
    print(f"Position created: {end}")
    distance: float = calculate_distance(origin, end)
    print(f"Distance between {origin} and {end}: {round(distance, 2)}\n")

    valid_input: str = "3,4,0"
    print(f"Parsing coordinates: \"{valid_input}\"")
    parsed_coord = parse_coordinates(valid_input)
    print(f"Parsed position: {parsed_coord}")
    if parsed_coord is not None:
        distance2: float = calculate_distance(origin, parsed_coord)
        print(f"Distance between {origin} and {parsed_coord}: "
              f"{round(distance2, 2)}\n")

    invalid_input: str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{invalid_input}\"")
    parse_coordinates(invalid_input)

    print()
    if parsed_coord is not None:
        print("Unpacking demonstration:")
        (x, y, z) = parsed_coord
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    coordinate_system()
