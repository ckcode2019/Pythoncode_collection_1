#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



# - Create an array variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Double all the values in the array and print the modified
#   array to the console as:
#   [6, 8, 10, 12, 14]


####### Solution #######


numbers = [3, 4, 5, 6, 7]

for indes_of_number_list, val_of_number_list in enumerate(numbers):
    numbers[indes_of_number_list] *= 2

print(numbers)