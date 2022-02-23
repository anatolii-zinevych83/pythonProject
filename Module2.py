#importing libraries
import string
from random import randint
from random import choice

#defining random number of dictionaries between 2 and 10
num_dict = randint(2, 10)
#defining random number of dictionary items between 0 and 25
num_entries = randint(0, 25)

#defining empty list
my_list = []
# opening cycle for dictionaries
for i in range(num_dict):
    #defining empty dictionary
    dictionary = {}
    # defining number of entries in the dictionary
    num_entries = randint(0, 25)
    #starting filling the dictionary with random key and value
    for j in range(num_entries):
        #defining that key is a string that contains ascii letters
        key: str = choice(string.ascii_letters)
        #switcing keys to lower case
        key1 = key.lower()
        #selecting value by random number between 0 and 100
        value = randint(0, 100)
        #binding key and value selected on previous step
        dictionary[key1] = value
    #appending next dictionary
    my_list.append(dictionary)
#printing initial list
print(my_list)

#defining empty temporary dictionary
new_dictionary = {}
#wakling through the dictionaries in a list
for dictionary in my_list:
    #walking through the items in the dictionary
    for k, v in dictionary.items():
        #filling new dictionary with all values for each key
        new_dictionary.setdefault(k, []).append(v)
#defining empty dictionary
final_dictionary = {}
#walking through dictionary items
for key, value in new_dictionary.items():
    #if number of values for key is more than 1
    if len(value) > 1:
        #selecting maximum value for key and adding its index
        final_dictionary[key+"_"+str(value.index(max(value))+1)] = max(value)
    else:
        #displaying key without index and value for this key
        final_dictionary[key] = value[0]
#printing final dictionary
print(final_dictionary)


















