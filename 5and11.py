num = int(input("enter a number : "))
if(num%5==0):
    if(num%10==0):
        print("divisible by 5 and 10")
    else:
        print("only divisible by 5")
else:
    print("neither divible by 5 nor 10")