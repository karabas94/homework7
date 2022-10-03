"""
1. Дано целое число (int). Определить сколько нулей в этом числе.
"""
number = int(input("Enter number: "))
# transformation integer to string
num_str = str(number)
# count zero in string
count = num_str.count('0')
print(f"Zero's in number: {count}")
