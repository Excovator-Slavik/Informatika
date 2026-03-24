
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
for month in range(1, months + 1):
    #Считаем сколько денег нужно в подушку безопастности
    nudodeneg = spend - salary
    #Таким образом копим убытки
    money_capital += nudodeneg
    # Увеличиваем траты для следующего месяца
    spend *= (1 + increase)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
