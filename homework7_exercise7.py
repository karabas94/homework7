"""
7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
"""
my_str = input("Enter string: ")
l_limit = input("Enter left limit: ")
r_limit = input("Enter right limit: ")
# find symbol from start string, +1 we don't print symbol
l_index = my_str.find(l_limit) + 1
# find symbol from end to star string
r_index = my_str.rfind(r_limit)
# string between left and right symbol
sub_str = my_str[l_index: r_index]
print(sub_str)
