"""
5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.[1,2,3,4] -> [2,3,4,1].
Пересоздавать список нельзя! (используйте метод pop)
"""
from random import randint

# random integer list with range ten
my_list = [randint(1, 200) for i in range(randint(1, 10))]
print(my_list)
# first element deleted and added last element
my_list.append(my_list.pop(0))
print(my_list)
