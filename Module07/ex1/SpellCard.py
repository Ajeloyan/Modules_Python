from ex0.Card import Card, Rarity
from enum import Enum


class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: Rarity, effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        game_state["available_mana"] -= self.cost
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "No specific effect"
        }
        if self.effect_type == SpellEffect.DAMAGE.value:
            result.update({
                "effect": f"Deal {self.cost} damage to target"
            })
        elif self.effect_type == SpellEffect.BUFF.value:
            result.update({
                "effect": f"Increase target attack +{self.cost}"
            })
        elif self.effect_type == SpellEffect.DEBUFF.value:
            result.update({
                "effect": f"Decrease target attack -{self.cost}"
            })
        elif self.effect_type == SpellEffect.HEAL.value:
            result.update({
                "effect": f"Heal target by {self.cost}hp"
            })
        return result

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "type": self.effect_type,
            "targets_affected": [target.name for target in targets],
            "status": "Effect resolved",
        }
