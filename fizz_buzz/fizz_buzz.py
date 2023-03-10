# Name: Charith Kumarasinghe
# Discode id: CHKUMARASINGH#1583

# programing task --

# Write a program that prints the numbers from 1 to 100
for i in range(1,101):
# For numbers which are multiples of both three and five print “FizzBuzz”
  if i % 3 ==0 and i % 5 == 0:
    print('FizzBuzz')
# but for multiples of three print “Fizz” instead of the number
  elif i % 3 == 0:
    print("Fizz")
# and for the multiples of five print “Buzz”
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)