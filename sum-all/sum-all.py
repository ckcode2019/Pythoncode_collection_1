#######################################
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583
# Practice assignment 2
#######################################



# - Create a variable named `numbers`
#   with the following content: `[3, 4, 5, 6, 7]`
# - Print the sum of the elements of `numbers`


####### Solution #######


numbers = [3, 4, 5, 6, 7]

sum_of_number_array = 0

for index_of_numbers, element_of_numbers in enumerate(numbers):
    sum_of_number_array += numbers[index_of_numbers]


print(sum_of_number_array)