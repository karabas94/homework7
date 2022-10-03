"""
6. Дана строка в которой есть числа (разделяются пробелами).Например "43 больше чем 34 но меньше чем 56".
Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.Для данного примера ответ - 133. (используйте split и проверку isdigit)
"""

my_str = input("Enter string: ")
sum = 0
# cycle for split string
for i in my_str.split():
    # check if splitted elements is integer
    if i.isdigit():
        # count sum integer elements
        sum += int(i)
print(sum)