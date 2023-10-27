users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
a = 0
b = 0
spisok = {
    'Общее количество': a,
    'Уникальные посещения': b
}
spisok['Общее количество'] = len(users)
spisok['Уникальные посещения'] = len(set(users))

print(spisok)