from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex0.Card import Card


class GameEngine:
    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = []
        self.battlefield: list[Card] = []
        self.game_state = {"available_mana": 10,
                           "turn_count": 0,
                           "max_mana": 10
                           }
        deck_info = self.factory.create_themed_deck(size=5)
        cards_dict = deck_info.get("content", {})
        self.deck = list(cards_dict.values())

        for _ in range(3):
            if self.deck:
                self.hand.append(self.deck.pop())

    def simulate_turn(self) -> dict:
        self.game_state["turn_count"] += 1
        self.game_state["available_mana"] = self.game_state["max_mana"]

        for card in self.battlefield:
            if hasattr(card, "has_attacked"):
                setattr(card, "has_attacked", False)

        if self.deck:
            self.hand.append(self.deck.pop())

        report = self.strategy.execute_turn(self.hand, self.battlefield)

        for card_name in report.get("cards_played", []):
            for card in list(self.hand):
                if card.name == card_name:
                    card.play(self.game_state)
                    self.hand.remove(card)
                    self.battlefield.append(card)
                    break

        self.battlefield = [c for c in self.battlefield
                            if getattr(c, "health", 1) > 0]

        return {
            "turn": self.game_state["turn_count"],
            "report": report,
            "status": self.get_engine_status()
        }

    def get_engine_status(self) -> dict:
        return {
            "mana": self.game_state["available_mana"],
            "deck_count": len(self.deck),
            "hand_count": len(self.hand),
            "battlefield_count": len(self.battlefield),
            "strategy": self.strategy.get_strategy_name()
        }
