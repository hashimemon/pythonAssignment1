import random
a=0
Rand_Number=0
print('You Have 3 chances to guess the number\n')
Rand_Number=int(random.randrange(1,30))
while a<3:
    userNumber=int(input("Enter number between 1 and 30: "))
    a+=1
    if Rand_Number>userNumber:
        print("Hidden number is greater\n")
    elif Rand_Number<userNumber:
        print("Hidden number is Smaller\n")
    else:
        print("You guess the correct Number")
        break
