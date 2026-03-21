from ex3.GameStrategy import GameStrategy
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard


class AgressiveStrategy(GameStrategy):
    def __init__(self) -> None:
        super().__init__()

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        remaining_mana = 10
        turn_report = {
            "cards_played": [],
            "mana_used": 0,
            "damage_dealt": 0,
            "targets_attacked": []
        }

        targets = self.prioritize_targets(battlefield)
        if not targets:
            return turn_report
        target = targets[0]

        def get_cost(card):
            return getattr(card, "cost", 0)
        sorted_hand = sorted(hand, key=get_cost)

        current_count = len([c for c in battlefield if
                             isinstance(c, CreatureCard)])

        for card in sorted_hand:
            if card.cost > 3 or card.cost > remaining_mana:
                continue
            if isinstance(card, CreatureCard) and current_count < 5:
                turn_report["cards_played"].append(card.name)
                turn_report["mana_used"] += card.cost
                remaining_mana -= card.cost
                current_count += 1

                attack_results = card.attack_target(target)
                turn_report["damage_dealt"] += \
                    attack_results.get("damage_dealt", 0)

                if target.name not in turn_report["targets_attacked"]:
                    turn_report["targets_attacked"].append(target.name)

            elif isinstance(card, SpellCard):
                turn_report["cards_played"].append(card.name)
                turn_report["mana_used"] += card.cost
                remaining_mana -= card.cost
                turn_report["damage_dealt"] += getattr(card, "power", 0)
                if target.name not in turn_report["targets_attacked"]:
                    turn_report["targets_attacked"].append(target.name)
        return turn_report

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:

        living_targets = []
        for target in available_targets:
            if getattr(target, "health", 0) > 0:
                living_targets.append(target)

        if not living_targets:
            return []

        def get_health(target):
            return getattr(target, "health", 999)

        return sorted(living_targets, key=get_health)
