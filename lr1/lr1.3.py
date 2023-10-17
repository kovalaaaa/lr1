list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

all_players = len(list_players)
index = all_players // 2
players_A = list_players[:index]
players_B = list_players[index:]

print(players_A)
print(players_B)
