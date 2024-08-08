# Assignment:
#Accept a string of Pairs of Peranthesis and check if 
# they are arranged properly. If so, print the number 
# of pairs of peranthesis else print improper arrangement.
# ((()())) : 4 pairs
# (()))	 : improper arrangement

def countParanthesis(paranthesis):
    count1=0
    count2=0
    for i in range(len(paranthesis)):
        if paranthesis[i] == '(':
            count1 += 1
        elif paranthesis[i] == ')':
            count2 += 1
            if count2 > count1 :
                print('Improper arrangement')
                break
        else:
            print('Invalid input') 
             
    if count1 == count2:
        print(f'{count1} pairs')
     
n_paranthesis = input('Enter paranthesis: ')
countParanthesis(n_paranthesis)