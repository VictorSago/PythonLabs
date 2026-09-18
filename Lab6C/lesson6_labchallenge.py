
# ==========================================================
# Lab 6 Challenge: Game Tournament Analytics System
# ==========================================================
# Restrictions followed: no classes, file handling, external libraries, Pandas, or NumPy.

# Part 1 - Tournament data
# The raw data intentionally contains inconsistent whitespace/capitalization.
raw_players = [
    {"name": "  anna ", "team": " phoenix", "country": "Sweden", "score": 1420, "matches": 12, "wins": 8, "active": True},
    {"name": "DAVID", "team": "Titans", "country": " sweden", "score": 1180, "matches": 10, "wins": 5, "active": True},
    {"name": " Sara", "team": "PHOENIX ", "country": "Spain", "score": 1560, "matches": 14, "wins": 10, "active": True},
    {"name": "leo ", "team": "Titans", "country": "SPAIN", "score": 990, "matches": 9, "wins": 2, "active": False},
    {"name": "MIA", "team": "Ravens", "country": "Germany", "score": 1310, "matches": 11, "wins": 6, "active": True},
    {"name": " noah", "team": "Ravens", "country": "germany ", "score": 870, "matches": 8, "wins": 0, "active": True},
    {"name": "Olivia ", "team": " Titans", "country": "France", "score": 1250, "matches": 13, "wins": 7, "active": True},
    {"name": "liam", "team": "PHOENIX", "country": "france", "score": 1040, "matches": 10, "wins": 3, "active": False},
    {"name": "EMMA ", "team": "Ravens", "country": "Sweden", "score": 1490, "matches": 15, "wins": 9, "active": True},
    {"name": "  lucas", "team": "Titans ", "country": "Norway", "score": 1120, "matches": 12, "wins": 4, "active": True},
    {"name": "sophia", "team": "Ravens", "country": "NORWAY", "score": 760, "matches": 7, "wins": 0, "active": False},
    {"name": "Ethan", "team": "Phoenix", "country": "Denmark", "score": 1370, "matches": 13, "wins": 8, "active": True},
    {"name": "ava ", "team": "Titans", "country": "denmark", "score": 1010, "matches": 9, "wins": 3, "active": True},
    {"name": "James", "team": "Ravens ", "country": "Finland", "score": 920, "matches": 8, "wins": 1, "active": False},
    {"name": "  isabella  ", "team": "Phoenix", "country": "FINLAND", "score": 1450, "matches": 14, "wins": 9, "active": True},
]


# Part 2 - Clean the player data
cleaned_players = [
    {
        **player,
        "name": player["name"].strip().title(),
        "team": player["team"].strip().title(),
        "country": player["country"].strip().title(),
    }
    for player in raw_players
]
print(cleaned_players)


# Part 3 - Filtering the tournament
print("--- Part 3 ---")
SCORE_THRESHOLD = 1300
SPECIFIC_COUNTRY = "Sweden"

active_players = [player for player in cleaned_players if player["active"]]
players_with_three_wins = [
    player for player in cleaned_players if player["wins"] >= 3
]
high_score_players = [
    player for player in cleaned_players if player["score"] > SCORE_THRESHOLD
]
players_from_country = [
    player for player in cleaned_players if player["country"] == SPECIFIC_COUNTRY
]
active_high_winners = [
    player for player in cleaned_players
    if player["active"] and player["wins"] >= 6
]
print("Active players:", active_players)
print("Players with at least 3 wins:", players_with_three_wins)
print("Players with a score above a threshold:", high_score_players)
print(f"Players from {SPECIFIC_COUNTRY}:", players_from_country)
print("Active players with at least 6 wins:", active_high_winners)


# Part 4 - Tournament statistics
print("--- Part 4 ---")
unique_countries = {player["country"] for player in cleaned_players}
unique_teams = {player["team"] for player in cleaned_players}
scores_by_player = {player["name"]: player["score"] for player in cleaned_players}
wins_by_player = {player["name"]: player["wins"] for player in cleaned_players}
high_score_players = {
    player["name"]: player["score"]
    for player in cleaned_players
    if player["score"] >= SCORE_THRESHOLD
}
print("Countres:", unique_countries)
print("Teams:", unique_teams)
print("Scores by player:", scores_by_player)
print("Wins by player:", wins_by_player)
print("High score players:", high_score_players)


# Part 5 - Combining the tournament data
print("--- Part 5 ---")
player_names = [player["name"] for player in cleaned_players]
ranking_points = [1200, 950, 1430, 1100, 1275, 880, 1190, 1010, 1380, 1140, 800, 1320, 990, 910, 1400]
bonus_points = [50, 20, 100, 30, 60, 10, 40, 25, 80, 45, 0, 70, 20, 15, 90]

ranking_points_by_player = {
    name: points for name, points in zip(player_names, ranking_points)
}
combined_player_points = [
    (name, ranking, bonus, ranking + bonus)
    for name, ranking, bonus in zip(player_names, ranking_points, bonus_points)
]
player_score_summary = [
    {"name": name, "tournament_score": score, "ranking_points": points}
    for name, score, points in zip(player_names, scores_by_player.values(), ranking_points)
]
short_zip_example = list(zip(["Alice", "Bob", "Carla"], [10, 20]))
# zip() stops when the shortest input collection is exhausted.
# Therefore, only two pairs are produced in short_zip_example.

print("Ranking points by player:", ranking_points_by_player)
print("Combined player points:", combined_player_points)
print("Player Score Summary:", player_score_summary)
print("Zipping unequal lists:", short_zip_example)


# Part 6 - Rankings
print("--- Part 6 ---")
ranking_by_score = sorted(cleaned_players, key=lambda player: player["score"], reverse=True)
ranking_by_wins = sorted(cleaned_players, key=lambda player: player["wins"], reverse=True)
ranking_by_matches = sorted(cleaned_players, key=lambda player: player["matches"], reverse=True)
ranking_by_name = sorted(cleaned_players, key=lambda player: player["name"])
ranking_by_score_asc = sorted(cleaned_players, key=lambda player: player["score"])
print("Players ranked by score, descending:", ranking_by_score)
print("Players ranked by wins:", ranking_by_wins)
print("Players ranked by matches:", ranking_by_matches)
print("Players sorted by name:", ranking_by_name)
print("Players ranked by score, ascending:", ranking_by_score_asc)



# Part 7 - Ranked tournament report
print("\nTOURNAMENT LEADERBOARD")
for position, player in enumerate(ranking_by_score, start=1):
    print(f"{position}. {player['name']} - {player['score']} points")


# Part 8 - Team analysis
print("--- Part 8 ---")
PARTICULAR_TEAM = "Phoenix"
MANY_WINS = 4
particular_team_players = [player["name"] for player in cleaned_players if player["team"] == PARTICULAR_TEAM]
players_with_many_wins = [
    player["name"] for player in cleaned_players if player["wins"] > MANY_WINS
]
active_players_above_threshold = {
    player["name"]: player["score"]
    for player in cleaned_players                                   # Can be simplified by using `active_players` from Part 3
    if player["active"] and player["score"] >= SCORE_THRESHOLD
}
print(f"All players in team {PARTICULAR_TEAM}: {particular_team_players}")
print(f"All players with more than {MANY_WINS} wins: {players_with_many_wins}")
print("Represented teams:", unique_teams)   # From Part 4
print("Represented countries:", unique_countries)   # From Part 4
print(f"Active players that reached the score of {SCORE_THRESHOLD}:", active_players_above_threshold)


# Part 9 - Player performance
# Performance rewards score and wins, while also considering match efficiency.
# The score is intentionally simple and transparent.
print("--- Part 9 ---")
TOP_PERFORMANCE_THRESHOLD = 1800

players_with_performance = [
    {
        **player,
        "performance": round(
            player["score"] + player["wins"] * 50
            + (player["wins"] / player["matches"]) * 100,
            2,
        ),
    }
    for player in cleaned_players
]
performance_ranking = sorted(
    players_with_performance,
    key=lambda player: player["performance"],
    reverse=True,
)
top_performers = performance_ranking[:5]
players_above_performance_threshold = [
    player for player in performance_ranking
    if player["performance"] >= TOP_PERFORMANCE_THRESHOLD
]
performance_by_player = {
    player["name"]: player["performance"] for player in players_with_performance
}
print("Players ranked by performance:", performance_ranking)
print("Top 5 performers:", top_performers)
print(f"Players performing above {TOP_PERFORMANCE_THRESHOLD}:", players_above_performance_threshold)
print("Performance for each player:", performance_by_player)
