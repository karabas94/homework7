"""
8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
Если строка содержит нечетное количество символов, пропущенный второй символ последней пары долженбыть заменен подчеркиванием ('_').
Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_'](используйте срезы длинны 2)
"""
my_str = input("Enter string: ")
my_result = []
# cycle for symbol in string with step two
for i in range(0, len(my_str), 2):
    # if index of string - 1 more than index of string with step 2
    if i < len(my_str) - 1:
        # two symbol add to string in my_result
        my_result.append(my_str[i] + my_str[i + 1])
    else:
        my_result.append(my_str[i] + '_')
print(my_result)
