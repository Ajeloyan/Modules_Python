def achi_analytics() -> None:
    alice_set: set = {
        "first_kill",
        "level_10",
        "treasure_hunter",
        "speed_demon",
    }
    bob_set: set = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie_set: set = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }
    uniques_achi: set = alice_set.union(bob_set, charlie_set)
    nb_uniques: int = len(uniques_achi)

    common_achi: set = alice_set.intersection(bob_set, charlie_set)

    other_than_alice = bob_set.union(charlie_set)
    other_than_bob = alice_set.union(charlie_set)
    other_than_charlie = alice_set.union(bob_set)

    uniques_alice = alice_set.difference(other_than_alice)
    uniques_bob = bob_set.difference(other_than_bob)
    uniques_charlie = charlie_set.difference(other_than_charlie)

    rares_achi = uniques_alice.union(uniques_bob, uniques_charlie)

    alice_bob = alice_set.intersection(bob_set)
    alice_bob_diff = alice_set.difference(bob_set)
    bob_alice_diff = bob_set.difference(alice_set)

    print("=== Achievement Tracker System ===\n")
    print(f"Player alice achievements: {alice_set}")
    print(f"Player bob achievements: {bob_set}")
    print(f"Player charlie achievements: {charlie_set}")
    print()
    print("=== Achievement Analytics ===")
    print(f"All unique achievements: {uniques_achi}")
    print(f"Total unique achievements: {nb_uniques}")
    print()
    print(f"Common to all players: {common_achi}")
    print(f"Rare achievements (1 player): {rares_achi}")
    print()
    print(f"Alice vs Bob common: {alice_bob}")
    print(f"Alice unique: {alice_bob_diff}")
    print(f"Bob unique: {bob_alice_diff}")


if __name__ == "__main__":
    achi_analytics()
