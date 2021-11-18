


char = input("Enter a character :")

ascii = ord(char)
if(ascii>48 and ascii<57):
    print(char, " is a number")
elif (ascii>64 and ascii<91) :
    print(char," is Uppercase" )
elif(ascii>96 and ascii<123):
    print(char," is a Lowercase" )
else:
    print(char," is a special character" )