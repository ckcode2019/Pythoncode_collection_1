#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



# - Create a two dimensional list (of strings)
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`
# - Print the array in the following format:
#
#   lime, forest green, oline, pale green, spring green
#   orange red, red, tomato
#   orchid, violet, pink, hot pink



####### Solution #######


# Two dimentional array(list) for colors.
two_dimentional_array = [
    ["lime", "forest green", "olive", "pale green", "spring green"],
    ["orange red", "red", "tomato"],
    ["orchid", "violet", "pink", "hot pink"]
    ]

# Please holder string variable.
combined_string = ""

# For loop to iterate main list.
for main_array_index in two_dimentional_array:
    # Sub array (list) iteration using "enumerate" function to get index and value. 
    for sub_array_index, sub_array_value in enumerate(main_array_index):
        if sub_array_index == 0:
            # Concatenating first element without ",".
            combined_string += sub_array_value
        else:
            # Concatenating rest of the elements with ",".
            combined_string += ", " + sub_array_value  
        
    # Printing the concatenated string. 
    print(combined_string)
    # Emptying sring for next iteration.
    combined_string = ""