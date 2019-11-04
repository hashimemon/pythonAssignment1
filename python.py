# Write a Python program to print the following string in a specific format (see the output).

poem = "Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are"
print(poem)


# Write a Python program to get the Python version you are using

import sys
pythonVersion = str(sys.version_info[0])+'.'+str(sys.version_info[1]);
print("You are using python : "+pythonVersion+" version");


# Write a Python program to display the current date and time.

from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)



# Write a Python program which accepts the radius of a circle from the user and compute the area.

from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

firstName = input("Please Enter your first name : ")
lastName = input("Please Enter your last name : ")
print(firstName[::-1]+' '+lastName[::-1])


# Write a python program which takes two inputs from user and print them addition

FirstNumber = input("Enter first number : ")
SecondNumber = input("Enter second number : ")
print(int(FirstNumber) + int(SecondNumber))1