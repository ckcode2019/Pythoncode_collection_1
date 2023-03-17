# - Create an array variable named `orders`
#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



#   with the following content: `["first", "second", "third"]`
# - Swap the first and the third element of `orders` programmatically
# - Print the swapped array into the console:
#   [third, second, first]



####### Solution #######



orders = ["first", "second", "third"]

first_element = orders[0]
third_element = orders[2]

orders[0] = third_element
orders[2] = first_element

print(orders)