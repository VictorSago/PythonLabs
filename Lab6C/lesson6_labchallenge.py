
# ==========================================================
# Lab 6 Challenge: Game Tournament Analytics System
# ==========================================================

# Restrictions followed: no classes, file handling, external libraries, Pandas, or NumPy.

# Part 1 - Tournament data
# The raw data intentionally contains inconsistent whitespace/capitalization.
raw_players = [
    {"name": "  anna ", "team": " phoenix", "country": "Sweden", "score": 142, "matches": 12, "wins": 8, "active": True},
    {"name": "DAVID", "team": "Titans", "country": " sweden", "score": 118, "matches": 10, "wins": 5, "active": True},
    {"name": " Sara", "team": "PHOENIX ", "country": "Spain", "score": 156, "matches": 14, "wins": 10, "active": True},
    {"name": "leo ", "team": "Titans", "country": "SPAIN", "score": 99, "matches": 9, "wins": 2, "active": False},
    {"name": "MIA", "team": "Ravens", "country": "Germany", "score": 131, "matches": 11, "wins": 6, "active": True},
    {"name": " noah", "team": "Ravens", "country": "germany ", "score": 87, "matches": 8, "wins": 0, "active": True},
    {"name": "Olivia ", "team": " Titans", "country": "France", "score": 125, "matches": 13, "wins": 7, "active": True},
    {"name": "liam", "team": "PHOENIX", "country": "france", "score": 104, "matches": 10, "wins": 3, "active": False},
    {"name": "EMMA ", "team": "Ravens", "country": "Sweden", "score": 149, "matches": 15, "wins": 9, "active": True},
    {"name": "  lucas", "team": "Titans ", "country": "Norway", "score": 112, "matches": 12, "wins": 4, "active": True},
    {"name": "sophia", "team": "Ravens", "country": "NORWAY", "score": 76, "matches": 7, "wins": 0, "active": False},
    {"name": "Ethan", "team": "Phoenix", "country": "Denmark", "score": 137, "matches": 13, "wins": 8, "active": True},
    {"name": "ava ", "team": "Titans", "country": "denmark", "score": 101, "matches": 9, "wins": 3, "active": True},
    {"name": "James", "team": "Ravens ", "country": "Finland", "score": 92, "matches": 8, "wins": 1, "active": False},
    {"name": "  isabella  ", "team": "Phoenix", "country": "FINLAND", "score": 145, "matches": 14, "wins": 9, "active": True},
]

# Part 2 - Clean the data without modifying raw_players.
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


# Part 3 - Filtering
SCORE_THRESHOLD = 130
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
