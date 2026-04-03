def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs) -> list:
        return f"{spell1(*args, **kwargs)}, {spell2(*args, **kwargs)}"
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def mult_power(*args, **kwargs) -> list:
        return (base_spell(*args, **kwargs) * multiplier)
    return mult_power


def conditional_caster(condition: callable, spell: callable) -> callable:
    def is_casting(*args, **kwargs) -> list:
        if condition(*args, **kwargs):
            return (spell(*args, **kwargs))
        else:
            return "Spell fizzled"
    return is_casting


def spell_sequence(spells: list[callable]) -> callable:
    def spells_caster(*args, **kwargs) -> list:
        return [spell(*args, **kwargs) for spell in spells]
    return spells_caster


def main() -> None:

    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {combined('Dragon')}")
    print()

    def fireball_power(power: int) -> int:
        return power

    print("Testing power amplifier...")
    base_power = 10
    mega_fireball = power_amplifier(fireball_power, 3)
    print(f"Original: {base_power}, Amplified: {mega_fireball(base_power)}")
    print()

    def is_finishable(health: int) -> bool:
        if health < 5:
            return True
        else:
            return False

    def finisher(health: int) -> str:
        return f"Health was {health}, now: 0"

    print("Testing conditional caster...")
    valid_health: int = 4
    invalid_health: int = 6
    conditional = conditional_caster(is_finishable, finisher)
    print(f"Testing with Dragon ({valid_health}hp):")
    print(f"{conditional(valid_health)}")
    print()
    print(f"Now with goblin ({invalid_health}hp):")
    print(f"{conditional(invalid_health)}")
    print()
    print("Testing spell_sequence...")

    def frostball(target: str) -> str:
        return f"Frostball hits {target}"

    def electricball(target: str) -> str:
        return f"Electricball hits {target}"

    spells = spell_sequence([frostball, electricball, fireball, heal])
    for s in spells("Dragon"):
        print(f"- {s}")


if __name__ == "__main__":
    main()
