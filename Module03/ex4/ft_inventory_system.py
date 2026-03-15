import sys


def inventory_system() -> None:
    if len(sys.argv) < 2:
        print("Please provide at least one item to analyze.")
        return

    inventory = {}

    for arg in sys.argv[1:]:
        parts = arg.split(':', 1)

        if len(parts) != 2 or not parts[1]:
            print(f"Skipping '{arg}': Invalid format "
                  "(expected item:quantity).")
            continue

        name, qty_str = parts

        try:
            quantity = int(qty_str)
        except ValueError:
            print(f"Skipping '{arg}': Quantity must be a valid number.")
            continue

        if quantity <= 0:
            print(f"Skipping '{name}': Quantity must be > 0 (got {quantity}).")
            continue

        inventory[name] = quantity

    if not inventory:
        print("Error: No valid data to analyze.")
        return

    print("=== Inventory System Analysis ===")
    total_items = sum(inventory.values())

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")

    displayed = {}
    categories: dict = {"Moderate": {}, "Scarce": {}}
    most_info = ""
    least_info = ""
    min_qty = -1

    for i in range(len(inventory)):
        highest_qty = -1
        highest_name = ""

        for name, qty in inventory.items():
            if name not in displayed and qty > highest_qty:
                highest_qty = qty
                highest_name = name

        if highest_name != "":
            percentage = (highest_qty / total_items) * 100
            print(f"{highest_name}: {highest_qty} units ({percentage:.1f}%)")

            if i == 0:
                most_info = f"{highest_name} ({highest_qty} units)"

            least_info = (f"{highest_name} ({highest_qty} "
                          f"unit{'s' if highest_qty > 1 else ''})")

            if min_qty == -1 or highest_qty < min_qty:
                min_qty = highest_qty

            if highest_qty > 3:
                categories["Moderate"].update({highest_name: highest_qty})
            else:
                categories["Scarce"].update({highest_name: highest_qty})

            displayed.update({highest_name: True})

    print("\n=== Inventory Statistics ===")
    print(f"Most abundant: {most_info}")
    print(f"Least abundant: {least_info}")

    print("\n=== Item Categories ===")
    print("Moderate:", categories.get("Moderate"))
    print("Scarce:", categories.get("Scarce"))

    print("\n=== Management Suggestions ===")
    print("Restock needed: ", end="")
    first = True
    for name, qty in inventory.items():
        if qty == min_qty:
            if not first:
                print(", ", end="")
            print(name, end="")
            first = False
    print()

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    print(f"Dictionary values: {', '.join(map(str, inventory.values()))}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    inventory_system()
