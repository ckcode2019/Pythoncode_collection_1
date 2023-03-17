#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Reverse the order of the elements of `numbers` programmatically
# - Print the elements of the reversed `numbers`:
#   [7, 6, 5, 4, 3]


####### Solution #######

# Import copy module to use deepcopy funciton
import copy

numbers = [3, 4, 5, 6, 7]

reversed_numbers = []

lenth_of_number_list = len(numbers)

# Iterating numbers list in reverse order
for i in range(1, lenth_of_number_list + 1):
    reversed_numbers.append(numbers[-i])


numbers = copy.deepcopy(reversed_numbers)

print(numbers)