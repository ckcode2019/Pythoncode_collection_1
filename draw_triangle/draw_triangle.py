
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --
# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

triangle_base = int(input("Enter value to create the triangle: "))
print("\n\n\n")
for i in range(0, triangle_base):
  print("*" * i +" " * (triangle_base -i))