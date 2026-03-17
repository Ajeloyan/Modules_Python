from ex0.Card import Rarity
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print()

    print("Testing Abstract Base Class Design:")
    print()

    dragon = CreatureCard("Fire dragon", 5, Rarity.LEGENDARY, 7, 5)

    print(f"{dragon.__class__.__name__} Info:")
    print(dragon.get_card_info())

    game_state = {"available_mana": 6}
    mana_available = game_state["available_mana"]
    print()

    print(f"Playing {dragon.name} with {mana_available} mana available:")
    playable = dragon.is_playable(mana_available)
    print(f"Playable: {playable}")

    if playable is True:
        result = (dragon.play(game_state))
        print(f"Play result: {result}")
    print()

    goblin = CreatureCard("Goblin Warrior", 6, Rarity.RARE, 5, 6)

    print(f"{dragon.name} attacks {goblin.name}:")
    print(f"Attack result: {dragon.attack_target(goblin)}")

    game_state["available_mana"] = 3
    mana_available = game_state["available_mana"]
    print()

    print(f"Testing insufficient mana ({mana_available} available):")
    playable = dragon.is_playable(mana_available)
    print(f"Playable: {playable}")
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
