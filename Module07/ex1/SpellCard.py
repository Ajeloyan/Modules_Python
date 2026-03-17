from ex0.Card import Card, Rarity


class SpellCard(Card):
    def __init__(
        self, name: str,
        cost: int,
        rarity: Rarity,
        effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state["available_mana"] -= self.cost
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": self.effect_type}

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "type": self.effect_type,
            "targets_affected": [target.name for target in targets],
            "status": "Effect resolved"
        }
