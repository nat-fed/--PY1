def get_count_char(str_):
    str_without_space = "".join(str_.lower().split())   # строка без пробелов и заглавных букв
    list_simbols = list(str_without_space)
    list_simbols.sort()

    simbol_in_str = {}
    count = 0

    for simbol in list_simbols:
        if simbol.isalpha():
            simbol_in_str[simbol] = simbol_in_str.get(simbol, count) + 1

    return simbol_in_str

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

def get_count_char_percent(dict_):
    total = sum(dict_.values())
    simbol_percent = {}
    for simbol, count in dict_.items():
        percent = round(count / total * 100, 2)
        simbol_percent[simbol] = simbol_percent.get(simbol, percent)

    return simbol_percent

print(get_count_char_percent(get_count_char(main_str)))
