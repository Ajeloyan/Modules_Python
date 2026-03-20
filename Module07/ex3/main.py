from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AgressiveStrategy
from ex0.CreatureCard import CreatureCard
from ex3.GameEngine import GameEngine
from ex0.Card import Rarity


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print()
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AgressiveStrategy()
    engine = GameEngine()

    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.__class__.__name__}")
    print(f"Available types: {factory.get_supported_types()}")
    print()

    enemy = CreatureCard("Enemy Player", 3, Rarity.COMMON, 3, 10)
    engine.battlefield = [enemy]

    print("Simulating aggressive turn...")

    hand_str = ", ".join([f"{c.name} ({c.cost})" for c in engine.hand])
    print(f"Hand: [{hand_str}]")
    print()

    print("Turn execution:")
    turn_result = engine.simulate_turn()

    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Actions: {turn_result['report']}")
    print()
    print("Game Report:")

    report = {
        "turns_simulated": turn_result["turn"],
        "strategy_used": strategy.get_strategy_name(),
        "total_damage": turn_result["report"]["damage_dealt"],
        "cards_created": len(engine.hand) + len(engine.battlefield)
        + len(engine.deck)
    }
    print(report)
    print()
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
