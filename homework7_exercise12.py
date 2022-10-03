"""
12. Даны две строки. Создать список в который поместить те символы,которые есть в обеих строках хотя бы раз.
"""
my_str_1 = input("Enter first string: ")
my_str_2 = input("Enter second string: ")
# string1 transformed to set1
set_1 = set(my_str_1)
# string2 transformed to set2
set_2 = set(my_str_2)
# intersection set1 and set2
my_set = set_1 & set_2
# intersection transformed to string
new_list = list(my_set)
print(new_list)