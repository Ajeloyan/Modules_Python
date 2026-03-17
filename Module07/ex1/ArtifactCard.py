from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(
        self, name: str,
        cost: int,
        rarity: Rarity,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        game_state["available_mana"] -= self.cost
        return {"card_played": self.name,
                "mana_used": self.cost,
                "effect": f"Permanent: {self.effect}"}

    def activate_ability(self) -> dict:
        return {
            "ability_activated": self.name,
            "effect_description": self.effect
        }
