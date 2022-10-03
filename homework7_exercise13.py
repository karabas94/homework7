"""
13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
но в каждой ТОЛЬКО ПО ОДНОМУ разу.Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"],
т.к. эти символы есть в каждой строке по одному разу
"""
my_str_1 = input("Enter first string: ")
my_str_2 = input("Enter second string: ")
my_list = []
# cycle for string 1
for i in my_str_1:
    # if one symbol in string1 and same one symbol in string2
    if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
        # my_list add symbol
        my_list.append(i)
print(my_list)
