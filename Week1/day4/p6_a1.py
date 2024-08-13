# 1. User gives the data like this:
#kerala-tiruvanantapuram karnataka-bengaluru tamilnadu-chennai
#You have to separate the states and store in the list states[] and also
#the seperated capitals must be stored in capitals[]


# def myFunction(user_given_list): 
#     state=[]
#     capital=[]
#     for i in user_given_list.split():
#       state,capital=user_given_list.split('-')
#     return state,capital

# state_capital = input('Enter the input data:')
# print(state_capital)
# state,capital=myFunction(state_capital)
# print('States:',state)
# print("Capitals:", capital)

def separate_states_and_capitals(data):
  """Separates states and capitals from a string."""
  states = []
  capitals = []
  for pair in data.split():
    state, capital = pair.split('-')
    states.append(state)
    capitals.append(capital)
  return states, capitals

# Get the input data
data = input("Enter the data: ")

# Separate states and capitals
states, capitals = separate_states_and_capitals(data)

# Print the results
print("States:", states)
print("Capitals:", capitals)