# 11. Print a hollow square of n line with the diagonals

lines=int(input('enter the number of lines:'))
for i in range(lines):
    for j in range(lines):
      if i == 0 or i == lines - 1 or j == 0 or j == lines - 1 or i == j and i + j == lines - 1:
        print("*", end="")
      else:
        print(" ", end="")
    print()