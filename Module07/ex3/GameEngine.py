from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self

    def simulate_turn(self) -> dict:
        pass

    def get_engine_status(self) -> dict:
        pass
