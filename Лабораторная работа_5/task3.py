from random import randint

def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 10
    count = 15
    list_numbers=[]
    if stop - start >= count:
        while len(list_numbers) < count:
            num = randint(start, stop)
            if num not in list_numbers:
                list_numbers.append(num)
    return list_numbers

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
