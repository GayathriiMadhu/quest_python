# Variable arguments

# def varArgFunction1(*arguments):
#     print(arguments)
#     print(type(arguments)) # tuple
 
# def varArgFunction2(*arguments):
#     for i in range(len(arguments)):
#         print(arguments[i])
 
# def varArgFunction2(*arguments):
#     for element in arguments: # for each loop. It accesses all elements of the tuple one by one
#         print(element)

# varArgFunction1(1, 2, 4)
# varArgFunction1()
# varArgFunction1('list', 'tuple', 'set', 'dictionary')
 
# varArgFunction2(1, 2, 4)
# varArgFunction2()
# varArgFunction2('list', 'tuple', 'set', 'dictionary')

#---------------------------------------------------------

# def varArgFunction1(*arguments):
#     print(arguments)
#     # arguments[1] = 22 # TypeError
#     arguments[5][0] = 20 # even though the list is inside the tuple, we can modify it.
#     print(arguments)
#     arguments[5].append(50)
#     print(arguments)
 
# varArgFunction1(1, 2, 4, 'list', 4.5, [2, 3, 5])
#------------------------------------------------------------

def varArgFunction(*arguments): # receives the data into a tuple. However, if it has objects like list or dictionary, then they will received by reference only.
    print(arguments)
    arguments[0].remove(10)
 
def myFunction(user_given_list): # receives refrence to the list numbers2
    user_given_list.remove(35)
 
numbers1 = [int(num) for num in input().split(',')]
# input: 10,20,30,40,50
varArgFunction(numbers1)# the list here is passed by reference
print(numbers1)
 
numbers2 = list(map(int, input().split()))
print(numbers2)
myFunction(numbers2)
print(numbers2)