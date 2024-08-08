# Program to print the Lucky number
def findSum(n) :
    sum = 0
    while n >= 10 :   # until the number is not a single digit number
        while n != 0 :
            sum = sum + (n % 10)
            n = n // 10
        
    return sum

n = int(input("Enter a number to find sum of its digits: "))
m = findSum(n)
print("Sum of the digits = ", m)
