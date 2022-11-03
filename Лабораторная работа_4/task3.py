def delete(list_, index=None):
    if index is None:
        list_.pop(-1)
    elif index == 0:
        list_.pop(0)
    elif index == -1:
        list_.pop(-1)
    else:
        list_end = list_[index + 1:]
        list_ = list_[:index + 1]
        list_.pop(-1)
        for i in list_end:
            list_.append(i)

    return list_

print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
