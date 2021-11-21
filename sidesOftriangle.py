
a = float(input('Enter length of side a: '))
b = float(input('Enter length of side b: '))
c = float(input('Enter length of side c: '))
if a+b>=c and b+c>=a and c+a>=b:
    print("valid sides")
else:
    print("invalid sides")
    