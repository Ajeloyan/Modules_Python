from ex0.Card import Card
import random


class Deck():
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        i = 0
        for card in self.cards:
            if card.name == card_name:
                self.cards.pop(i)
                return True
            i += 1
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total: int = len(self.cards)

        stats: dict = {
            "total_cards": total,
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0.0
        }

        if total == 0:
            return stats

        total_cost = 0
        for card in self.cards:
            total_cost += card.cost

            class_name = card.__class__.__name__
            if class_name == "CreatureCard":
                stats["creatures"] += 1
            if class_name == "SpellCard":
                stats["spells"] += 1
            if class_name == "ArtifactCard":
                stats["artifacts"] += 1

        stats["avg_cost"] = total_cost / total

        return stats
