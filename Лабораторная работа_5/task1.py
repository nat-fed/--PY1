from pprint import pprint

stop = 15
list_ = [{"bin": bin(num), "dec": num, "hex": hex(num), "oct": oct(num)} for num in range(stop + 1)]

pprint(list_)
