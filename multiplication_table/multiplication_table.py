# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Create a program that asks for a number and prints the multiplication table with that number
#
# Example:
# The number 15 should print:
#
# 1 * 15 = 15
# 2 * 15 = 30
# 3 * 15 = 45
# 4 * 15 = 60
# 5 * 15 = 75
# 6 * 15 = 90
# 7 * 15 = 105
# 8 * 15 = 120
# 9 * 15 = 135
# 10 * 15 = 150

required_number = int(input("Enter the number you want to print the multiplication table: "))
print()
expected_range = int(input("What is the maximum multiplier you need ex; 10, 12, 24: "))
print("\n\n")

for i in range(1, expected_range + 1):
  print(f"{i} * {required_number} = {i * required_number} " )