# importing libraries
import string
from random import randint
from random import choice


def selecting_random_range(start_num, end_num):
    random_range = randint(start_num, end_num)
    return random_range



def creating_list_of_dictionaries():
    my_list = []
    for i in range(selecting_random_range(2, 10)):
        dictionary = {}
        for j in range(selecting_random_range(0, 25)):
            key: str = choice(string.ascii_letters)
            key1 = key.lower()
            value = selecting_random_range(0, 100)
            dictionary[key1] = value
        my_list.append(dictionary)
    return my_list


def creating_temporary_dictionary(my_list):
    new_dictionary = {}
    for dictionary in my_list:
        for k, v in dictionary.items():
            new_dictionary.setdefault(k, []).append(v)
    return new_dictionary


def creating_final_dictionary(new_dictionary):
    final_dictionary = {}
    for key, value in new_dictionary.items():
        if len(value) > 1:
            final_dictionary[key + "_" + str(value.index(max(value)) + 1)] = max(value)
        else:
            final_dictionary[key] = value[0]
    return final_dictionary


my_list = creating_list_of_dictionaries()
print(my_list)

new_dictionary = creating_temporary_dictionary(my_list)

final_dictionary = creating_final_dictionary(new_dictionary)
print(final_dictionary)
