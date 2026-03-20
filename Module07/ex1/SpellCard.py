from ex0.Card import Card, Rarity
from enum import Enum


class SpellEffect(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        effect_type: str,
        power: int
    ) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type
        self.power = power

    def play(self, game_state: dict) -> dict:
        game_state["available_mana"] -= self.cost
        result = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "No specific effect",
        }
        if self.effect_type == SpellEffect.DAMAGE.value:
            result.update({"effect": f"Deal {self.power} damage to target"})
        elif self.effect_type == SpellEffect.BUFF.value:
            result.update({"effect": f"Increase target attack +{self.power}"})
        elif self.effect_type == SpellEffect.DEBUFF.value:
            result.update({"effect": f"Decrease target attack -{self.power}"})
        elif self.effect_type == SpellEffect.HEAL.value:
            result.update({"effect": f"Heal target by {self.power}hp"})
        return result

    def resolve_effect(self, targets: list) -> dict:
        for target in targets:
            if self.effect_type == SpellEffect.DAMAGE.value:
                target.health -= self.power
        return {
            "spell": self.name,
            "type": self.effect_type,
            "power": self.power,
            "targets_affected": [target.name for target in targets],
            "status": "Effect resolved",
        }
