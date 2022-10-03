"""
2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
"""
number = int(input("Enter number: "))
# transformation integer to string
num_str = str(number)
count = 0
# cycle for count "0" from end to start string
for i in num_str[::-1]:
    if i == "0":
        count += 1
    else:
        # cycle stop if elements from string not "0"
        break
print(count)