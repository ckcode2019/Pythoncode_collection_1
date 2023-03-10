# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --
#Print the Body mass index (BMI) based on these values
print("BMI calculator \n\n")

weight = float(input(f"Enter your weight in (kg): \n"))
height = float(input(f"Enter your height in (m):  \n"))
print()

bmi= round((weight / height ** 2), 2) 

print(f"Your BMI value is: {bmi}")