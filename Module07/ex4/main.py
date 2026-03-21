from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")
    print()
    platform = TournamentPlatform()
    try:
        dragon = TournamentCard(
            name="Fire Dragon",
            cost=5,
            rarity=Rarity.LEGENDARY,
            attack_val=12,
            health_val=10,
            card_id="dragon_001",
            defense_val=4,
            rating=1200
        )

        wizard = TournamentCard(
            name="Ice Wizard",
            cost=4,
            rarity=Rarity.RARE,
            attack_val=8,
            health_val=7,
            card_id="wizard_001",
            defense_val=2,
            rating=1150
        )

        for card in [dragon, wizard]:
            platform.register_card(card)

            interfaces = [base.__name__ for base in card.__class__.__bases__]

            stats = card.get_rank_info()
            print(f"{card.name} (ID: {card.card_id}):")
            print(f"- Interfaces: [{', '.join(interfaces)}]")
            print(f"- Rating: {stats['rating']}")
            print(f"- Record: {stats['record']}")
            print()

        print("Creating tournament match...")
        match_result = platform.create_match("dragon_001", "wizard_001")
        print(f"Match result: {match_result}")
        print()

        print("Tournament Leaderboard:")
        leaderboard = platform.get_leaderboard()
        for i, card in enumerate(leaderboard, 1):
            stats = card.get_rank_info()
            print(f"{i}. {card.name} - Rating: "
                  f"{stats['rating']} ({stats['record']})")
        print()
        print("Platform Report:")

        report = platform.generate_tournament_report()
        print(report)
        print()
        print("=== Tournament Platform Successfully Deployed! ===")
        print("All abstract patterns working together harmoniously!")
    except (ValueError, KeyError) as e:
        print(f"\n[CRITICAL ERROR] {e}")
        print("Platform deployment aborted.")


if __name__ == "__main__":
    main()
