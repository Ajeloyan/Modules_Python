from ex4.TournamentCard import TournamentCard


class TournamentPlatform():
    def __init__(self) -> None:
        self.cards = {}
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        if card.card_id in self.cards:
            raise ValueError(f"Card with ID {card.card_id} is already "
                             "registered")
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        self.match_played += 1
        c1 = self.cards[card1_id]
        c2 = self.cards[card2_id]
        hp1, hp2 = c1.health_val, c2.health_val

        rounds = 0
        while hp1 > 0 and hp2 > 0 and rounds < 20:
            rounds += 1
            res_c2 = c2.defend(c1.attack(c2)["damage"])
            hp2 -= res_c2["damage_taken"]
            if hp2 <= 0:
                break
            res_c1 = c1.defend(c2.attack(c1)["damage"])
            hp1 -= res_c1["damage_taken"]
        if hp1 > hp2:
            winner, loser = c1, c2
        else:
            winner, loser = c2, c1
        winner.update_wins(1)
        loser.update_losses(1)
        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        def get_rating(card):
            return card.calculate_rating()

        all_cards = list(self.cards.values())
        sorted_cards = sorted(all_cards, key=get_rating, reverse=True)
        return sorted_cards

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)
        total_rating = 0
        for card in self.cards.values():
            total_rating += card.calculate_rating()

        avg_rating = 0
        if total_cards > 0:
            avg_rating = total_rating // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self.match_played,
            "avg_rating": avg_rating,
            "platform_status": "active"
        }
