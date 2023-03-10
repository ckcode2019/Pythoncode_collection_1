
# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

pyramid_base = int(input("Enter value to create the diamond: "))
print("\n\n\n")
for i in range(0, pyramid_base):
  print(" " * (pyramid_base-i)+ "*" * i + "*" + "*" * i +" " * (pyramid_base -i))