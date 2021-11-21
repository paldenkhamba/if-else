#checking if the user is elligible to vote or not 
date  = input("enter date (yy/mm/dd):")
#splitting
d = date.split("/")
if(int(d[0])<2003):
    if(int(d[1])<12):
        if(int(d[2])<31):
            print("you can vote")
        else:
            print("invalid input")
    else:
        print("invalid input")
else:
    print("you are not elligible")

#checking age 
current_date=[2021,11,19]
age = 0
if (int(d[1])<current_date[1]):
     age= current_date[0]-int(d[0])
else:
    age= current_date[0]-int(d[0])-1

print("your age is : ",age)
print(current_date[0])