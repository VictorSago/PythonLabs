
# ==========================================================
# Lab 6 Challenge: Game Tournament Analytics System
# ==========================================================
# Restrictions followed: no classes, file handling, external libraries, Pandas, or NumPy.

# Helper functions for printing player dicts as well 
# as dicts with different internal structure
def format_dict_values(data, fields=None, bool_labels=None, sep=" - "):
    """Return a single-line summary of any dict's values, joined by `separator`.

    Works regardless of which keys are present. `fields` optionally selects
    and orders which keys to include (defaults to all of the dict's keys,
    in their existing order). Boolean values are converted to a readable
    label instead of True/False; `bool_labels` lets specific keys use
    custom wording (e.g. {"active": ("Active", "Inactive")}), and any
    other boolean falls back to "Yes"/"No".
    """
    bool_labels = bool_labels or {}
    keys = fields if fields is not None else data.keys()

    parts = []
    for key in keys:
        value = data[key]
        if isinstance(value, bool):
            active_label, inactive_label = bool_labels.get(key, ("Yes", "No"))
            value = active_label if value else inactive_label
        parts.append(str(value))

    return sep.join(parts)


def format_dict_list(dicts, fields=None, bool_labels=None, sep=" - "):
    """Return a multi-line string: a header line of key names, then one
    formatted dict per line, all joined using `separator`.
    """
    if not dicts:
        return ""

    header_keys = fields if fields is not None else dicts[0].keys()
    header = sep.join(header_keys)

    rows = "\n".join(
        format_dict_values(d, fields, bool_labels, sep) for d in dicts
    )
    return f"{header}\n{rows}"


def format_player(player, fields=None, separator=" - "):
    """Return a single-line summary of one player dict."""
    return format_dict_values(
        player, fields=fields, bool_labels={"active": ("Active", "Inactive")}, sep=separator
    )


def format_player_list(players, fields=None, separator=" - "):
    """Return a header line plus one formatted player per line."""
    return format_dict_list(
        players, fields=fields, bool_labels={"active": ("Active", "Inactive")}, sep=separator
    )


# Part 1 - Tournament data
# The raw data intentionally contains inconsistent whitespace/capitalization.
raw_players = [
    {"name": "  anna ", "team": " phoenix", "country": "Sweden", "score": 1420, "matches": 12, "wins": 12, "active": True},
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
# print(format_player_list(cleaned_players))


# Part 3 - Filtering the tournament
# print("--- Part 3 ---")
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
# print("Active players:")
# print(format_player_list(active_players))
# print("Players with at least 3 wins:")
# print(format_player_list(players_with_three_wins))
# print(f"Players with a score above a {SCORE_THRESHOLD}:")
# print(format_player_list(high_score_players))
# print(f"Players from {SPECIFIC_COUNTRY}:")
# print(format_player_list(players_from_country))
# print("Active players with at least 6 wins:")
# print(format_player_list(active_high_winners))


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
print("Countries:", unique_countries)
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

# print("Ranking points by player:", ranking_points_by_player)
# print("Combined player points:", combined_player_points)
print("Player Score Summary:")
print(format_dict_list(player_score_summary))
# print("Zipping unequal lists:", short_zip_example)


# Part 6 - Rankings
# print("--- Part 6 ---")
ranking_by_score = sorted(cleaned_players, key=lambda player: player["score"], reverse=True)
ranking_by_wins = sorted(cleaned_players, key=lambda player: player["wins"], reverse=True)
ranking_by_matches = sorted(cleaned_players, key=lambda player: player["matches"], reverse=True)
ranking_by_name = sorted(cleaned_players, key=lambda player: player["name"])
ranking_by_score_asc = sorted(cleaned_players, key=lambda player: player["score"])
# print("Players ranked by score, descending:")
# print(format_player_list(ranking_by_score))
# print("Players ranked by wins:")
# print(format_player_list(ranking_by_wins))
# print("Players ranked by matches:")
# print(format_player_list(ranking_by_matches))
# print("Players sorted by name:")
# print(format_player_list(ranking_by_name))
# print("Players ranked by score, ascending:")
# print(format_player_list(ranking_by_score_asc))


# Part 7 - Ranked tournament report
print("\nTOURNAMENT LEADERBOARD")
for position, player in enumerate(ranking_by_score, start=1):
    print(f"{position}. {format_player(player, fields=['name', 'score'])} points")


# Part 8 - Team analysis
# print("--- Part 8 ---")
PARTICULAR_TEAM = "Phoenix"
MANY_WINS = 4
particular_team_players = [player["name"] for player in cleaned_players if player["team"] == PARTICULAR_TEAM]
players_with_many_wins = [
    player["name"] for player in cleaned_players if player["wins"] > MANY_WINS
]
active_players_above_threshold = {
    player["name"]: player["score"]
    for player in active_players
    if player["score"] >= SCORE_THRESHOLD
}
# print(f"All players in team {PARTICULAR_TEAM}: {particular_team_players}")
# print(f"All players with more than {MANY_WINS} wins: {players_with_many_wins}")
# print("Represented teams:", unique_teams)   # From Part 4
# print("Represented countries:", unique_countries)   # From Part 4
# print(f"Active players that reached the score of {SCORE_THRESHOLD}:", active_players_above_threshold)


# Part 9 - Player performance
# Performance rewards score and wins, while also considering match efficiency.
# The score is intentionally simple and transparent.
# print("--- Part 9 ---")
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
# print("Players ranked by performance:", performance_ranking)
# print("Top 5 performers:", top_performers)
# print(f"Players performing above {TOP_PERFORMANCE_THRESHOLD}:", players_above_performance_threshold)
# print("Performance for each player:", performance_by_player)


# Final Challenge - Tournament Analytics Report
# Final report helpers
def print_player_list(title, players, fields=None):
    print(f"\n{title}")
    for position, player in enumerate(players, start=1):
        if isinstance(player, dict):
            print(f"{position}. {format_player(player, fields=fields)}")
        else:
            print(f"{position}. {player}")


# Three additional analyses
nowin_players = [player["name"] for player in cleaned_players if player["wins"] == 0]
undefeated_players = [
    player["name"] for player in cleaned_players
    if player["matches"] == player["wins"]
]
players_by_country = {
    country: [player["name"] for player in cleaned_players if player["country"] == country]
    for country in unique_countries
}

team_average_scores = {}
for team in unique_teams:
    team_scores = [player["score"] for player in cleaned_players if player["team"] == team]
    team_average_scores[team] = round(sum(team_scores) / len(team_scores), 2)


# Final report
print("\nTOURNAMENT ANALYTICS REPORT")
print(f"Total number of players: {len(cleaned_players)}")
print(f"Number of active players: {len(active_players)}")
print(f"Unique teams: {', '.join(sorted(unique_teams))}")
print(f"Unique countries: {', '.join(sorted(unique_countries))}")

print_player_list("Players ranked by score", ranking_by_score, fields=["name", "score"])
print_player_list("Players ranked by wins", ranking_by_wins, fields=["name", "wins"])
print_player_list("Top 5 players", ranking_by_score[:5], fields=["name", "score"])
print_player_list(
    f"Players above performance threshold ({TOP_PERFORMANCE_THRESHOLD})",
    players_above_performance_threshold,
    fields=["name", "performance"]
)

print("\nADDITIONAL ANALYSIS")
print(f"Players with no wins: {', '.join(nowin_players) or 'None'}")
print(f"Players with no losses: {', '.join(undefeated_players) or 'None'}")
print(f"Average score by team: {team_average_scores}")
print(f"Players by country: {players_by_country}")


# Pythonic Design Review
# 
# Example 1: cleaned_players (Part 2)
# Longer version would have looked like:
#   cleaned_players = []
#   for player in raw_players:
#       cleaned_player = dict(player)
#       cleaned_player["name"] = player["name"].strip().title()
#       cleaned_player["team"] = player["team"].strip().title()
#       cleaned_player["country"] = player["country"].strip().title()
#       cleaned_players.append(cleaned_player)
# Technique used: list comprehension with dict unpacking.
# Why the final version is clearer:
#   The comprehension keeps "build a new list of transformed dictionaries"
#   as one expression, instead of splitting it across an empty-list init,
#   a manual copy, three assignments and an append call.
#
# Example 2: unique_countries (Part 4)
# Longer version would have looked like:
#   unique_countries = set()
#   for player in cleaned_players:
#       unique_countries.add(player["country"])
# Technique used: set comprehension.
# Why the final version is clearer:
#   `{player["country"] for player in cleaned_players}` signals immediately
#   that only distinct values are wanted; the init-then-add loop requires
#   reading the whole block to notice it's a set, not a list, being built.
#
# Example 3: scores_by_player (Part 4)
# Longer version would have looked like:
#   scores_by_player = {}
#   for player in cleaned_players:
#       scores_by_player[player["name"]] = player["score"]
# Technique used: dictionary comprehension.
# Why the final version is clearer:
#   The name -> score mapping is stated directly as key: value, rather than
#   an empty-dict init plus a separate assignment line buried in the loop body.
#
# Example 4: Tournament Leaderboard (Part 7)
# Longer version would have looked like:
#   print("\nTOURNAMENT LEADERBOARD")
#   position = 1
#   for player in ranking_by_score:
#       print(f"{position}. {player['name']} - {player['score']} points")
#       position += 1
# Technique used: enumerate().
# Why the final version is clearer:
#   enumerate(..., start=1) removes the manual counter variable that would
#   otherwise have to be initialized and incremented with the loop by hand.


# Deliberately over-complicated comprehension:
# complicated = [
#     player["name"] for player in cleaned_players
#     if player["active"] and player["score"] > 1200
#     and player["wins"] >= 5 and player["country"] in {"Sweden", "Spain", "Germany"}
# ]
#
# Clearer version: name the conditions and use a normal loop.
selected_countries = {"Sweden", "Spain", "Germany"}
qualified_names = []
for player in cleaned_players:
    is_qualified = (
        player["active"]
        and player["score"] > 1200
        and player["wins"] >= 5
        and player["country"] in selected_countries
    )
    if is_qualified:
        qualified_names.append(player["name"])
# The clearer version separates the condition from the collection-building
# step, rather than cramming four chained conditions onto one comprehension
# line where they're hard to scan.
print("Qualified names example for complicated selection:", qualified_names)
