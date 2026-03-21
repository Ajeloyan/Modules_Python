from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
import sys


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print()

    game_state = {"available_mana": 10}
    try:
        cards: list = [
            CreatureCard("Fire dragon",
                         5,
                         Rarity.LEGENDARY,
                         7,
                         5),
            SpellCard("Lightning Bolt",
                      3,
                      Rarity.UNCOMMON,
                      "damage",
                      4),
            ArtifactCard("Mana crystal",
                         4,
                         Rarity.RARE,
                         6,
                         "+1 mana per turn"),
        ]
        deck = Deck()
        for card in cards:
            deck.add_card(card)
    except Exception as e:
        print(e)
        sys.exit(1)

    print("Building deck with different card types...")
    print(f"Deck stats: {deck.get_deck_stats()}")
    print()

    while True:
        try:
            card = deck.draw_card()

            card_type = card.__class__.__name__
            print(f"Drew: {card.name} ({card_type})")
            result = card.play(game_state)
            print(f"Play result: {result}")
            print()
        except IndexError:
            break
    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
