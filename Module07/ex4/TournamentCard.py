from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: Rarity,
                 attack_val: int,
                 health_val: int,
                 card_id: str,
                 defense_val: int,
                 rating: int):
        Card.__init__(self, name, cost, rarity)
        if not isinstance(attack_val, int) or attack_val <= 0:
            raise ValueError("attack must be a positive integer")
        self.attack_val = attack_val
        if not isinstance(health_val, int) or health_val <= 0:
            raise ValueError("health must be a positive integer")
        self.health_val = health_val
        if not isinstance(defense_val, int) or defense_val <= 0:
            raise ValueError("defense must be a positive integer")
        self.defense_val = defense_val
        if not isinstance(rating, int) or rating <= 0:
            raise ValueError("rating must be a positive integer")
        self.rating = rating
        self.wins = 0
        self.losses = 0
        self.card_id = card_id

    def play(self, game_state: dict) -> dict:
        game_state["available_mana"] -= self.cost
        return {
            "card_played": self.name,
            "cost": self.cost,
            "status": "active on battlefield"
        }

    def get_card_info(self) -> dict:
        return {
            "type": "Creature",
            "attack": self.attack_val,
            "health": self.health_val
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self.cost

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.attack_val
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = incoming_damage - self.defense_val
        if damage_taken < 0:
            damage_taken = 0
        damage_blocked = incoming_damage - damage_taken
        still_alive = True
        if (self.health_val - damage_taken) <= 0:
            still_alive = False
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_val,
            "defense": self.defense_val,
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "wins": self.wins,
            "losses": self.losses,
            "rating": self.calculate_rating()
        }
