from ex3.CardFactory import CardFactory
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Any
import random
from ex0.Card import Rarity
from ex1.SpellCard import SpellEffect


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures = {
            "dragon": {
                "name": "Fire Dragon",
                "cost": 5,
                "rarity": Rarity.LEGENDARY,
                "attack": 7,
                "health": 5,
            },
            "goblin": {
                "name": "Goblin Warrior",
                "cost": 2,
                "rarity": Rarity.COMMON,
                "attack": 4,
                "health": 5,
            },
        }

        self.spells = {
            "fireball": {
                "name": "Fireball",
                "cost": 4,
                "rarity": Rarity.UNCOMMON,
                "effect_type": SpellEffect.DAMAGE,
            },
            "lightning": {
                "name": "Lightning Bolt",
                "cost": 3,
                "rarity": Rarity.UNCOMMON,
                "effect_type": SpellEffect.DAMAGE,
            }
        }

        self.artifacts = {
            "amulet": {
                "name": "Amulet of Vigor",
                "cost": 3,
                "rarity": Rarity.RARE,
                "durability": 4,
                "effect": "Passive: All friendly creatures gain +1 Attack",
            }
        }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self.creatures:
            data = self.creatures[name_or_power]
            return CreatureCard(data["name"],
                                data["cost"],
                                data["rarity"],
                                data["attack"],
                                data["health"])

        if isinstance(name_or_power, int):
            for data in self.creatures.values():
                if data["attack"] == name_or_power:
                    return CreatureCard(data["name"],
                                        data["cost"],
                                        data["rarity"],
                                        data["attack"],
                                        data["health"])

        raise ValueError(f"no creature card found with {name_or_power}")

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self.spells:
            data = self.spells[name_or_power]
            return SpellCard(data["name"],
                             data["cost"],
                             data["rarity"],
                             data['effect_type'])

        if isinstance(name_or_power, int):
            for data in self.spells.values():
                if data["cost"] == name_or_power:
                    return SpellCard(data["name"],
                                     data["cost"],
                                     data["rarity"],
                                     data['effect_type'])

        raise ValueError(f"no spell card found with {name_or_power}")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if isinstance(name_or_power, str) and name_or_power in self.artifacts:
            data = self.artifacts[name_or_power]
            return ArtifactCard(data["name"],
                                data["cost"],
                                data["rarity"],
                                data["durability"],
                                data["effect"])

        if isinstance(name_or_power, int):
            for data in self.artifacts.values():
                if data["durability"] == name_or_power:
                    return ArtifactCard(data["name"],
                                        data["cost"],
                                        data["rarity"],
                                        data["durability"],
                                        data["effect"])
        raise ValueError(f"no artifact card found with {name_or_power}")
