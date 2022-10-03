"""
11. Дана строка my_str. Создать список в который поместить те символы из my_str,которые встречаются в строке ТОЛЬКО ОДИН раз.
"""

my_str = input("Enter string: ")
my_list = []
# cycle for string
for i in my_str:
    # if symbol only one
    if my_str.count(i) == 1:
        # my_list add symbol
        my_list.append(i)
print(my_list)
