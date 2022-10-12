list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_num = max(list_numbers) # Максимальное число в спике
max_index = list_numbers.index(max_num) # Индекс максимального числа в списке

list_numbers[max_index], list_numbers[-1] = list_numbers[-1], max_num # TODO Оформить решение

print(list_numbers)

