from random import randint


def get_unique_list_numbers(start=-10, stop=10, size=15) -> list[int]:
    list_ = []
    while len(list_) < size:
        i = randint(start, stop)
        if i not in list_:
            list_.append(i)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
