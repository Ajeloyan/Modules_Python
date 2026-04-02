def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"],
                  reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {}
    mage_max_power = max(mages, key=lambda mage: mage["power"])
    mage_min_power = min(mages, key=lambda mage: mage["power"])
    mage_avg_power: float = round(sum(map(lambda mage: mage['power'], mages)) / len(mages), 2)
    max_power = mage_max_power["power"]
    min_power = mage_min_power["power"]
    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': mage_avg_power
    }


def main() -> None:
    artifacts: list[dict] = [
        {'name': 'Storm Crown', 'power': 117, 'type': 'relic'},
        {'name': 'Crystal Orb', 'power': 73, 'type': 'relic'},
        {'name': 'Wind Cloak', 'power': 113, 'type': 'relic'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'accessory'}]
    mages: list[dict] = [
        {'name': 'Casey', 'power': 73, 'element': 'ice'},
        {'name': 'Sage', 'power': 59, 'element': 'wind'},
        {'name': 'River', 'power': 85, 'element': 'fire'},
        {'name': 'Nova', 'power': 77, 'element': 'lightning'},
        {'name': 'Phoenix', 'power': 75, 'element': 'water'}]
    spells: list[str] = ['heal', 'blizzard', 'darkness', 'fireball']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    check_first = 1
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)", end=" ")
        if check_first == 1:
            print("comes before", end=" ")
            check_first += 1
        else:
            if check_first != len(sorted_artifacts):
                print("and then", end=" ")
                check_first += 1
            else:
                print()
    print()
    print("Testing spell transformer...")
    spells_list = spell_transformer(spells)
    for i, spell in enumerate(spells_list):
        if i < len(spells_list) - 1:
            print(spell, end=" ")
        else:
            print(spell)
    print()

    print("Testing power filter...")
    print(power_filter(mages, 80))
    print()

    print("Testing mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
