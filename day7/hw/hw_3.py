# program do zadanie nr 3
from pprint import pprint

from player_stats import load_file, get_players_sorted_by_column, get_most_common_name, get_averages

data = load_file()
top_players = get_players_sorted_by_column(data)
pprint(top_players[:3])
# sredni wiek graczy
pprint(get_averages(data))
most_common_names = get_most_common_name(data)
# srednia ilsoc punktow zdobytych przez graczy
pprint(get_averages(data, column_name='score'))
# pprint(most_common_names[:3])
pprint(top_players[0])
pprint(top_players[-1])
players_sorted_by_age = get_players_sorted_by_column(data, column_name='age')
pprint(players_sorted_by_age[0])
pprint(players_sorted_by_age[-1])
