money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить


while money_capital + salary > spend:
    spend += spend * increase
    delta = salary - spend
    money_capital += delta
    month += 1
   # TODO Оформить решение

print(month)

