from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex2.EliteCard import EliteCard, CombatStyle
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import sys


def main() -> None:
    print("=== DataDeck Ability System ===")
    print()
    card_meth = [method for method in dir(Card) if not method.startswith("_")]
    comb_meth = [method for method in dir(Combatable)
                 if not method.startswith("_")]
    magical_meth = [method for method in dir(Magical)
                    if not method.startswith("_")]
    print(f"Card: {card_meth}")
    print(f"Combatable: {comb_meth}")
    print(f"Magical: {magical_meth}")
    print()

    try:
        arcane_war = EliteCard("Arcane Warrior", 7, Rarity.LEGENDARY,
                           CombatStyle.MELEE, 5, 3, 8, 10, 4)
        print(f"Playing {arcane_war.name} ({arcane_war.__class__.__name__})")
        enemy = CreatureCard("Enemy", 5, Rarity.UNCOMMON, 5, 7)
    except Exception as e:
        print(e)
        sys.exit(1)
    print()

    print("Combat phase:")
    print(arcane_war.attack(enemy))
    print(arcane_war.defend(5))
    print()

    print("Magic phase:")
    print(arcane_war.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print(arcane_war.channel_mana(3))
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
