from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard


class AgressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        super().__init__()

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        if not hand:
            return {"action": "pass", "card_played": None}
        selected_card = hand[0]
        min_cost = getattr(selected_card, "cost", 999)
        for card in hand:
            current_cost = getattr(selected_card, "cost", 999)

            if current_cost < min_cost:
                min_cost = current_cost
                selected_card = card

            elif current_cost == min_cost:
                if getattr(card, "attack", 0) > getattr(selected_card, "attack", 0):
                    selected_card = card

        return {
            "strategy": self.get_strategy_name(),
            "action": "play",
            "card_played": selected_card.name
        }

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if not available_targets:
            return []

        def get_health(target):
            return getattr(target, "health", 999)
        return sorted(available_targets, key=get_health)
