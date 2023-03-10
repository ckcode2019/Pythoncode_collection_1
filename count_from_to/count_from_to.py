# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
def which_number_is_biger():
    number_one=int(input("Please enter number one: ? "))
    number_two=int(input("Please enter number two: ? "))
    print()
    if number_two < number_one:
        print("Number two should be biger than number one lets restart! \n\n")
        which_number_is_biger()
# If it is bigger it should count from the first number to the second by one
    else:
        for i in range (number_one , (number_two + 1) ):
            print(f"{i}")
which_number_is_biger()       
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5
# 5