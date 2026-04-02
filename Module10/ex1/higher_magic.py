def fireball(target: str) -> str:
    return (f"fireball hits {target}")


def heal(target: str) -> str:
    return (f"{target} healed")


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    pass


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    pass


def conditional_caster(condition: callable, spell: callable) -> callable:
    pass


def spell_sequence(spells: list[callable]) -> callable:
    pass
