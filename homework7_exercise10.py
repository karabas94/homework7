"""
10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
Например [1, 2, 3, "11", "22", 33]Создать новый список в который поместить только строки из my_list.
"""
my_list = [1, 2, 3, "11", "22", 33]
print(my_list)
new_list = []
# cycle for list
for i in my_list:
    # if type of elements string
    if type(i) == str:
        # new_list add str elements
        new_list.append(i)
print(new_list)
