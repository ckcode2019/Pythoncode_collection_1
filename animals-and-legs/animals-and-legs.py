
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --
# Write a program that asks for two integers

# The first represents the number of chickens the farmer has
number_of_chickens = int(input("Enter number of chickens 🐔 farmer has: \n"))

# The second represents the number of pigs owned by the farmer
number_of_pigs = int(input("Enter number of pigs 🐖 farmer has: \n"))

# It should print how many legs all the animals have
number_of_legs_chiken_have = number_of_chickens * 2
number_of_legs_pigs_have = number_of_pigs * 4

count_legs_all_animals_have = number_of_legs_chiken_have + number_of_legs_pigs_have

print(f"The farmar have {number_of_chickens} chickens 🐔 and their leg count is {number_of_legs_chiken_have} \n ")
print(f"The farmar have {number_of_pigs} pigs🐖 and their leg count is {number_of_legs_pigs_have} \n ")
print(f"Total number of animals 🐔🐖 famer have is {number_of_chickens + number_of_pigs} and they have { number_of_legs_chiken_have + number_of_legs_pigs_have} legs")
