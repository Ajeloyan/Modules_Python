def mage_counter() -> callable:
    counter: int = 0

    def counter_times() -> int:
        nonlocal counter
        counter += 1
        return counter
    return counter_times


def spell_accumulator(initial_power: int) -> callable:
    power: int = 0

    def power_increase() -> int:
        nonlocal power
        power += (initial_power)
        return power
    return power_increase


def enchantment_factory(enchantment_type: str) -> callable:
    if enchantment_type == "Frozen":
        def enchantment_frozen(item_name: str) -> str:
            return f"{enchantment_type} {item_name}"
        return enchantment_frozen
    elif enchantment_type == "Flaming":
        def enchantment_flaming(item_name: str) -> str:
            return f"{enchantment_type} {item_name}"
        return enchantment_flaming
    elif enchantment_type == "Electric":
        def enchantment_electric(item_name: str) -> str:
            return f"{enchantment_type} {item_name}"
        return enchantment_electric
    else:
        def unknown_enchantment(item_name: str) -> str:
            return f"Can't enchant {item_name} with '{enchantment_type}' "
        "(unknown)"
        return unknown_enchantment


def memory_vault() -> dict[str, callable]:
    memory: dict = {}

    def recall(key: str) -> callable | str:
        value = memory.get(key)
        if not value:
            return "Memory not found"
        else:
            return value

    def store(key: str, value: callable) -> None:
        memory.update(key, value)

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter: callable = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}: {counter()}")
    print()

    
    print("Testing enchantment factory...")
    print(enchantment_factory("Flaming")("Sword"))
    print(enchantment_factory("Frozen")("Shield"))
    print(enchantment_factory("Electric")("Helmet"))
    print(enchantment_factory("wrong")("Axe"))
    print()
    print("Testing spell_accumulator...")
    initial_power = 10
    spell_acc = spell_accumulator(initial_power)
    print(f"Initial power = {initial_power}")
    print()
    for i in range(1, 4):
        print(f"Call {i}: Power = {spell_acc()}")
    print()
    print("Testing memory vault...")



if __name__ == "__main__":
    main()
