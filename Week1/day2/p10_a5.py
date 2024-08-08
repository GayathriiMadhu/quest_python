# 5. Print an equi lateral triangle of n lines

lines=int(input('enter the number of lines:'))
number=lines
for i in range(1, number + 1):
    print(" " * (number - i), end="")
    print("*" * (2 * i - 1))