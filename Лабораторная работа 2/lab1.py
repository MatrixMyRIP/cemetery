money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

months = 0
while True:
    ost = spend - salary
    if ost > money_capital:
        break

    months += 1
    money_capital -= ost
    spend = spend * (1 + increase)

# months = 0
# while money_capital != 0 or money_capital + salary < spend:
#     money = money_capital - (spend - salary)
#     if money <= 0:
#         break
#     months += 1
#     spend_1 = spend * (1 + increase)
#     money_capital = money_capital - spend_1
print("Количество месяцев, которое можно протянуть без долгов:", months)
