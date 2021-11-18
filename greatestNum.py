num1 = int(input("Enter first num :"))
num2 = int(input("Enter second num :"))
num3 = int(input("Enter third num :"))
if(num1>num3):
    if(num1>num2):
        print(num1," is the greatest number ")
elif (num3>num2):
    print(num3, " is the greatest number")
else:
    print(num2 ," is the greates number")
