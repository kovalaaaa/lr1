import json

def task() -> float:
    with open(r'.\input.json', 'r', encoding='utf-8') as file:
        a = json.load(file)
    sum = 0
    for i in a:
        sum += i['score']*i['weight']
    return round(sum, 3)


print(task())
