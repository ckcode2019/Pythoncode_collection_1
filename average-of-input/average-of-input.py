# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Write a program that asks for 5 integers in a row,
number_array = []
for i in range(0,5):
    number = int(input(f"Please enter number {i + 1}: \n" ))
    number_array.append(number)

sum_of_given_numbers = sum(number_array)
print(f"Sum of number {number_array[0]}, {number_array[1]}, {number_array[2]}, {number_array[3]}, {number_array[4]} is: {sum_of_given_numbers} \n")

# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
print(f"The average of given numbers is: {sum_of_given_numbers/5}")    


