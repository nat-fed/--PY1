salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

list_months = list(range(1, (months + 1)))

for i in list_months:
    if i < 2:
        delta = salary - spend
        need_money += abs(delta)
    else:
        spend += spend * increase
        delta = salary - spend
        need_money += abs(delta)
# TODO Оформить решение

print(round(need_money))

