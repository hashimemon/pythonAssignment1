con='y'
while con!='n':
    age=int(input("Enter age : "))
    if age>12:
        print("Ticket is 15$")
    elif age>=3:
        print("Ticket is 10$")
    else:
        print("Ticket is free")
    con=input("Are you want to take ticket y/n: ")
