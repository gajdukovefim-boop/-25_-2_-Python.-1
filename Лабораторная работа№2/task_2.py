salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_needed = 0  # Общая сумма, которую нужно взять из подушки безопасности
current_spend = spend
for month in range(months):
    shortage = current_spend - salary
    if shortage > 0:
        money_needed += shortage
    current_spend *= (1 + increase)
money_needed = round(money_needed)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_needed)
