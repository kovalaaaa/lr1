money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
all_spend = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while True:
    all_spend = all_spend + spend * ((1 + increase) ** months)
    months += 1
    if salary * months + money_capital < all_spend:
        months -= 1
        break
print("Количество месяцев, которое можно протянуть без долгов:", months)
