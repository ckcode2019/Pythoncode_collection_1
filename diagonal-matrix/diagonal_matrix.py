#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



# Write a program that asks for an integer n,
# then it creates a two-dimensional array (of integers) of the specified
# size (nxn) with the value of 1 on the main diagonal and the value of 0
# everywhere else. Print the 2d array into the output
#
# Example:
#
# Please enter the array (matrix) size: 4
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1


####### Solution #######

# User input of diagonal diamention
user_input = int(input("Enter positive integer: "))
# Define list for diagonal diamentions
main_list = []
sub_list = []

# Iteration to place "1" in each sub list comptible index of main list index using user input. 
# # Main list will have n* userinput elements.
for sub_list_indexes in range(0, user_input):
    for sublist_values in range(0, user_input):
        # Compair sub list index with main list index to position the "1"
        if sub_list_indexes == sublist_values:
            sub_list.append(1)
        else:
            sub_list.append(0)
    # Appending above created sub list to main list
    main_list.append(sub_list)
    # Emptying sublist for next iteration.
    sub_list = []

# Create a empty string for concatenate the sub list values as a srting   
concateneted_sublist = ""
# Iterate main string to concatenate using enuemrate function.
for main_list_index, main_list_values_as_a_sub_list in enumerate(main_list):
  for sub_list_value in main_list_values_as_a_sub_list:
    # Type caste and concatenate sublist value
    concateneted_sublist += str(sub_list_value)
  # Print the concatenate vlue of each sub list
  print(concateneted_sublist)
  # Emptying string for next iteration of main list element
  concateneted_sublist = ""


