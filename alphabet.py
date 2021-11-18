from typing_extensions import IntVar


char = input("Enter a character :")
ascii = ord(char)
if (ascii>64 and ascii<91) :
    print(char," is an alphabet" )
elif(ascii>96 and ascii<123):
    print(char," is an alphabet" )
else:
    print(char," is not an alphabet" )