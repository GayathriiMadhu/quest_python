#Accept the food type (veg or non-veg) from the user and then
# prompt her for the food item number and serve her the food.
#self


# veg_food_items = {
#     1 : 'Veg Fried rice',
#     2 : 'Roti - dal',
#     3 : 'Jeera rice - Paneer butter masala',
#     4 : 'Special Poha',
#     5 : 'Veg Mushroom Biryani'
# }

# Non_veg_food_items = {
#     1 : 'Chicken Fried rice',
#     2 : 'Roti - Kadai Chicken',
#     3 : 'Jeera rice - Chicken butter masala',
#     4 : 'Sea food meals',
#     5 : 'Chicken Biryani'
# }

# print('Welcome to our hotel')
# print('1:Vegetarian 2:Non- Vegetarian')
# food_type_number = int(input('Enter the food type number that you wish:'))

# if food_type_number==1:
#     print('1:Fried rice 2:Roti 3:Jeera rice 4:Poha 5:Biriyani')
#     food_item_number = int(input('Enter the food item number that you wish:'))
#     if food_item_number < 1 or food_item_number > 5:
#         print('Invalid choice entered')
#     else:
#         print('Your ' + veg_food_items.get(food_item_number) + ' is here')

# elif food_type_number==2:
#     print('1:Fried rice 2:Roti 3:Jeera rice 4:Meals 5:Biriyani')
#     food_item_number = int(input('Enter the food item number that you wish:'))
#     if food_item_number < 1 or food_item_number > 5:
#         print('Invalid choice entered')
#     else:
#         print('Your ' + Non_veg_food_items.get(food_item_number) + ' is here')
# else:
#     print('Invalid choice entered')

# print('Thank you, Visit again')




#Accept the food item number from the user and serve him the food.
import sys
 
veg_food_items = {
    1 : 'Mysuru Filter Coffee',
    2 : 'Yummy Idly-vada',
    3 : 'Worlds soft Mysuru Mailari Dosa',
    4 : 'Bhupal Special Poha',
    5 : 'Bengaluru tamato-peanuts Upama'
}
non_veg_food_items = {
    1 : 'Egg Pokoda',
    2 : 'Chicken Biryani',
    3 : 'Fish Fry',
    4 : 'Mutton Masala'
}
food_types = {
    1 : veg_food_items,
    2 : non_veg_food_items
}
food_items = {
    1 : '1:Coffee 2:Idly-Vada 3:Dosa 4:Poha 5:Upama',
    2 : '1:Egg Pokoda 2:Chicken Biryani 3:Fish Fry'
}
 
print('Welcome to our hotel The Taste')
user_choice = int(input('1:Veg 2:Non-Veg \n Your choice please: '))
items = food_items.get(user_choice, 'Invalid')
if items == 'Invalid':
    sys.exit('Invalid choice entered')
print(items)
food_item_number = int(input('Enter the food item number that you wish:'))
 
print('Your ' + food_types.get(user_choice).get(food_item_number) + ' is here')
 
print('Thank you, Visit again')

# ########################################################################################3

import sys
 
veg_food_items = {
    1 : 'Mysuru Filter Coffee',
    2 : 'Yummy Idly-vada',
    3 : 'Worlds soft Mysuru Mailari Dosa',
    4 : 'Bhupal Special Poha',
    5 : 'Bengaluru tamato-peanuts Upama'
}
non_veg_food_items = {
    1 : 'Egg Pokoda',
    2 : 'Chicken Biryani',
    3 : 'Fish Fry',
    4 : 'Mutton Masala'
}
food_types = {
    1 : veg_food_items,
    2 : non_veg_food_items
}
food_items = {
    1 : '1:Coffee 2:Idly-Vada 3:Dosa 4:Poha 5:Upama',
    2 : '1:Egg Pokoda 2:Chicken Biryani 3:Fish Fry'
}
 
print('Welcome to our hotel The Taste')
 
while True:
    user_choice = int(input('1:Veg 2:Non-Veg \t Your choice please: '))
    items = food_items.get(user_choice, 'Invalid')
    if items == 'Invalid':
        print('Invalid choice entered')
        break
    print(items)
    food_item_number = int(input('Enter the food item number that you wish:'))
 
    print('Your ' + food_types.get(user_choice).get(food_item_number) + ' is here')
    user_choice = int(input('Do you wish to have more: Press 1 if yes: '))
    if user_choice != 1:
        break
print('Thank you, Visit again')