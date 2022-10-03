"""
9. Дан список чисел. Определите, сколько в этом списке элементов,которые больше суммы двух своих соседей (слева и справа)
, и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
"""
from random import randint

# random integer list with range 10
my_list = [randint(1, 10) for i in range(randint(1, 10))]
print(my_list)
count = 0
# cycle for second elements to last but one
for i in range(1, len(my_list) - 1):
    # sum elements bigger than elements from right and left
    if my_list[i] > my_list[i - 1] + my_list[i + 1]:
        # count how many elements bigger than elements from right and left
        count += 1
print(count)
