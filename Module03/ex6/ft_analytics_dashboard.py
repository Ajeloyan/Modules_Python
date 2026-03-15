from typing import Any

if __name__ == "__main__":
    players_data: dict[str, dict[str, Any]] = {
        'alice': {'player_name': 'alice',
                  'total_score': 2300,
                  'online': True,
                  'region': 'north',
                  'achievements': ['first_blood',
                                   'level_master',
                                   'speed_runner',
                                   'treasure_seeker',
                                   'boss_hunter']},

        'bob': {'player_name': 'bob',
                'total_score': 1800,
                'online': True,
                'region': 'north',
                'achievements': ['boss_hunter',
                                 'explorer']},

        'charlie': {'player_name': 'charlie',
                    'total_score': 2150,
                    'online': True,
                    'region': 'east',
                    'achievements': ['level_master',
                                     'speed_runner',
                                     'treasure_seeker',
                                     'boss_hunter',
                                     'pixel_perfect',
                                     'combo_king',
                                     'explorer']},

        'diana': {'player_name': 'diana',
                  'total_score': 2050,
                  'online': False,
                  'region': 'central',
                  'achievements': ['first_blood',
                                   'pixel_perfect',
                                   'combo_king',
                                   'explorer']},
    }
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")
    high_scores: list[str] = [
        player["player_name"]
        for player in players_data.values() if player['total_score'] > 2000
    ]
    print(f"High scorers (>2000): {high_scores}")

    scores_doubled: list[int] = [
        player["total_score"]*2
        for player in players_data.values()
    ]
    print(f"Scores doubled: {scores_doubled}")

    active_players: list[str] = [
        player["player_name"]
        for player in players_data.values() if player["online"] is True
    ]
    print(f"Active players: {active_players}")
    print()

    print("=== Dict Comprehension Examples ===")

    players_scores: dict = {
        player["player_name"]: player["total_score"]
        for player in players_data.values()
    }
    print(f"Player scores: {players_scores}")

    scores_cat: dict[str, int] = {
        "high": sum([1 for player in players_data.values()
                     if player["total_score"] > 2100]),
        "medium": sum([1 for player in players_data.values()
                       if 1900 < player["total_score"] < 2100]),
        "low": sum([1 for player in players_data.values()
                    if player["total_score"] < 1900])
    }
    print(f"Score categories: {scores_cat}")

    achi_count: dict = {
        player["player_name"]: len(player["achievements"])
        for player in players_data.values()
    }
    print(f"Achievement counts: {achi_count}")
    print()

    print("=== Set Comprehension Examples ===")

    unique_players: set = {
        player["player_name"]
        for player in players_data.values()
    }
    print(f"Unique players: {unique_players}")

    unique_achievements: set = {
        achievements
        for infos in players_data.values()
        for achievements in infos["achievements"]
    }
    print(f"Unique achievements: {unique_achievements}")

    regions: set = {
        player["region"] for player in players_data.values()
    }
    print(f"Active regions: {regions}")
    print()

    print("=== Combined Analysis ===")
    print(f"Total players: {len(unique_players)}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    scores: list[int] = [score for score in players_scores.values()]
    avg_scores = float(sum(scores) / len(scores))
    print(f"Average score: {avg_scores:.1f}")
    top_name = max(players_scores, key=players_scores.get)
    top_info = players_data[top_name]
    print(f"Top performer: {top_name} ({top_info['total_score']} points, "
          f"{len(top_info['achievements'])} achievements)")
