from ex0.Card import Rarity
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Magical, Combatable):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: Rarity,
        combat_type: str,
        attack_pwr: int,
        defense_pwr: int,
        mana_pool: int,
        health: int,
        spell_cost: int
    ) -> None:
        super().__init__(name, cost, rarity)
        if health <= 0:
            raise ValueError("Health has to be positive")
        if attack_pwr < 0:
            raise ValueError("attack_pwr has to be positive")
        if defense_pwr < 0:
            raise ValueError("defense_power cannot be negative")
        self.combat_type = combat_type
        self.attack_pwr = attack_pwr
        self.defense_pwr = defense_pwr
        self.mana_pool = mana_pool
        self.health = health
        self.spell_cost = spell_cost

    def play(self, game_state: dict) -> dict:
        game_state["available_mana"] -= self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card entered the field"
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_pwr,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage - self.defense_pwr
        if damage_taken < 0:
            damage_taken = 0
        damage_blocked = incoming_damage - damage_taken
        still_alive = True
        if (self.health - damage_taken) <= 0:
            still_alive = False
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_pwr,
            "defense": self.defense_pwr,
            "combat_type": self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        self.mana_pool -= self.spell_cost
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.spell_cost
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool
        }
