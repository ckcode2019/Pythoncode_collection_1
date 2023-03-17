#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



# - Create a variable named `firstArrayOfNumbers`
#   with the following content: `[1, 2, 3]`
# - Create a variable named `secondArrayOfNumbers`
#   with the following content: `[4, 5]`
# - Print "secondArrayOfNumbers is longer" if `secondArrayOfNumbers` has more
#   elements than `firstArrayOfNumbers`
# - Otherwise print: "firstArrayOfNumbers is the longer one"



####### Solution #######

# Initiation of "firstArrayOfNumbers" and "secondArrayOfNumbers" lists
firstArrayOfNumbers = [1, 2, 3]
secondArrayOfNumbers = [4, 5]

# Function checking wich list is longer
def check_which_variable_is_longer(v_one, v_two):
    # Get list range
    len_v_one = len(v_one)
    len_v_two = len(v_two)

    # Check which list has the most elements
    if len_v_one > len_v_two:
        print("firstArrayOfNumbers is the longer one")
    else:
        print("secondArrayOfNumbers is longer")

# Calling function 
check_which_variable_is_longer(firstArrayOfNumbers, secondArrayOfNumbers)