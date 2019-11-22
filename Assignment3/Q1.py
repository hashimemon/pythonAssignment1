ans = None
num1 = int(input("Enter first value: "))
num2 = int(input("Enter second value: "))

choice = input("\nEnter your choice(+,-,*,/,**): ")

if choice == '+':
    ans = num1+num2
elif choice == '-':
    ans = num1-num2
elif choice == '*':
    ans = num1*num2
elif choice == '/':
    ans = num1/num2
elif choice == '**':
    ans = num1**num2
    
print(f"\nAnswer : {ans}")
