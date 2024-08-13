# 10. Print X shape made up of stars of n lines

lines=int(input('enter the number of lines:'))
for i in range(lines):
    for j in range(lines):
      if i == j or i + j == lines - 1:
        print("* ", end="")
      else:
        print("  ", end="")
    print()