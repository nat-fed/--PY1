from random import randint

def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    count = 15
    list_numbers = [randint(start, stop) for _ in range(count)] # Список случайных целых числе от -10 до 10 включительно

    list_temp = []
    list_numbers_all = list(range(start, stop + 1))
    for x in list_numbers_all:
        if x not in list_numbers:
            list_temp.append(x)

    for i in list_numbers:
        if list_numbers.count(i) != 1:
            list_numbers[list_numbers.index(i)] = list_temp[-1]
            list_temp.pop(-1)

    return list_numbers
    # TODO написать функцию для получения списка уникальных целых чисел


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
