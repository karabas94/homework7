"""
4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list стоит на последнем месте.
 Если my_list [1,2,3,4], то new_list [2,3,4,1]
"""
from random import randint

# random integer list with range five
my_list = [randint(1, 200) for i in range(randint(1, 5))]
print(my_list)
# my_list copied to new_list
new_list = my_list.copy()
# first and last elements changed
new_list[0], new_list[-1] = new_list[-1], new_list[0]
print(new_list)
