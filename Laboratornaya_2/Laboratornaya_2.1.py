money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0 #месяца
i = 0 #разница
while True:
    i = spend - salary
    if i > money_capital:
        break
    months += 1
    money_capital -= i
    spend *= 1 + increase
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
