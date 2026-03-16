def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    is_valid: str = validate_ingredients(ingredients)
    if "VALID" in is_valid:
        return f"Spell recorded: {spell_name} ({is_valid})"
    else:
        return f"Spell rejected: {spell_name} ({is_valid})"
