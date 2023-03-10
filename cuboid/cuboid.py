# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Write a program that stores 3 sides of a cuboid as variables (float)
# The program should write the surface area and volume of the cuboid like:
# 
length=float(input("Enter value for Length: "))
width=float(input("Enter value for Width: "))
height=float(input("Enter value for Height: "))
print()

surface= int (round( ((length * width * 2) + (length * height * 2 ) + ( width * height * 2)),0))
volume= int(round( (length * width * height), 0 ))
# Surface Area: 600
# Volume: 1000

print(f"Surface of the cuboid id {surface} \n")
print(f"Volume of the cuboid id {volume} \n")
