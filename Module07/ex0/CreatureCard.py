from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: Rarity, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("Attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("Health must be a positive integer")
        self.attack = attack
        self.health = health
        self.has_attacked = False

    def play(self, game_state: dict) -> dict:
        game_state["available_mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        if hasattr(target, 'health'):
            target.health -= self.attack
            self.has_attacked = True

        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "target_health_remaining": target.health,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
