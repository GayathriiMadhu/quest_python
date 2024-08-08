# perfect square bills get discount
import math
customers = int(input('Enter the number of customers: '))
bills = []
for i in range (customers):
    print(f'Enter the bill-{i+1} amount : ')
    amount = int(input())
    bills.append(amount)
#print(f'The bill amounts are : {bills}')
count_of_perfect_squares = 0
for i in range(customers):
    root=math.isqrt(bills[i])
    if (root * root == bills[i]):
        count_of_perfect_squares +=1
print(f'{count_of_perfect_squares} are eligible for discount')

#----------------------------------------------------------------------
# import math
# N = int(input("The no:of customers:"))
# bill_amounts = []
# count_of_perfect_squares = 0
# print(f'Enter the bill amounts of {N} customers :')
# for i in range(N):
#     amount = int(input())
#     bill_amounts.append(amount)
# print(f'Customer bill amounts are: {bill_amounts}')
# for i in range(N):
#     root = math.isqrt(bill_amounts[i])
#     if(root * root == bill_amounts[i]):
#         count_of_perfect_squares += 1
# print(f'Count of perfect squares of {N} bills is {count_of_perfect_squares}')