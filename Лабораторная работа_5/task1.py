# TODO решить с помощью list comprehension и распечатать его
stop = 15
list_ = [{"bin": bin(num), "dec": num, "hex": hex(num), "oct": oct(num)} for num in range(stop + 1)]

from pprint import pprint

pprint(list_)
