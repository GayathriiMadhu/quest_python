# 5. Demonstrate the different ways of adding elements to a 
# list and different ways to delete elements from a list

#1. Append :Adds an element to the end of the list.

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  

#2. Insert: Inserts an element at a specific index.

my_list = [1, 3, 4]
my_list.insert(1, 2)  # Inserts 2 at index 1
print(my_list)  


#3. Extend: Adds multiple elements from another iterable (like a list, tuple, or string) to the end of the list.

my_list = [1, 2]
other_list = [3, 4]
my_list.extend(other_list)
print(my_list)  

#########################################################################
#Deleting Elements from a List

#1. Remove: Removes the first occurrence of a specified value.

my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  

# 2. Pop: Removes and returns the element at a specified index. 
# If no index is specified, removes and returns the last element.

my_list = [1, 2, 3]
removed_element = my_list.pop(1)  # Removes and returns 2
print(my_list)  
print(removed_element)  

#3. Del: Deletes an element or a slice of elements from a list.

my_list = [1, 2, 3, 4]
del my_list[1]  # Deletes the element at index 1
print(my_list)
  
del my_list[1:3]  # Deletes elements from index 1 to 2 (exclusive)
print(my_list)  