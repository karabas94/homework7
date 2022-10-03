"""
3.Даны списки my_list_1 и my_list_2.Создать список my_result в который вначале поместитьэлементы на четных местах из my_list_1,
а потом все элементы на нечетных местах из my_list_2.
"""
from random import randint

# random integer list1 with range five
my_list_1 = [randint(1, 200) for i in range(5)]
print(my_list_1)
# random integer list1 with range five
my_list_2 = [randint(1, 200) for k in range(5)]
print(my_list_2)
my_result = []
# cycle for even and uneven index
for j in range(len(my_list_1)):
    # add even to my my_result
    my_result.append(my_list_1[j])
    for h in range(j, j+1):
        # add uneven to my_result
        my_result.append(my_list_2[h])
print(my_result)
