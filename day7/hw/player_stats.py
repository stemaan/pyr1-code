import csv
from collections import Counter


def load_file(filename='players.csv'):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def get_players_sorted_by_column(players, column_name='score'):
    # sort sorts in place
    # players.sort(key=lambda player: player['score'], reverse=True)
    players_sorted_by_score = sorted(players, key=lambda player: player[column_name],
                                     reverse=True)  # def ?(player): return player['score']
    return players_sorted_by_score


def get_averages(players, column_name='age'):
    total = 0
    for player in players:
        total += int(player[column_name])

    return total / len(players)


def get_most_common_name(players):
    names = []
    for player in players:
        full_name = player['name']
        # ['imie', 'nazwisko']
        firstname = full_name.split(' ')[0]
        names.append(firstname)
    names_counter = Counter(names)
    names_sorted = names_counter.most_common()
    return names_sorted
