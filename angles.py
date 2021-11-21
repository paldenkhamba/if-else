num=1 
sum = 0
print("enter angles of a triangle : ")
while(num<4):
    angle = int(input("angle :"))
    sum = sum+angle
    num=num+1
if(sum==180):
    print("valid angles")
else:
    print("invalid angles")
    