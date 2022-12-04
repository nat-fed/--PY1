import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, "r") as f:
        list_ = [line.rstrip().split(",") for line in f]
        headers_list = list_[0]
        rows = list_[1: len(list_)]
        list_dict = []
        for rows_list in rows:
            dict_ = dict(zip(headers_list, rows_list))
            list_dict.append(dict_)
    return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
