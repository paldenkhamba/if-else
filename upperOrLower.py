
char = input("Enter a character :")
ascii = ord(char)
if (ascii>64 and ascii<91) :
    print(char," is an Upper Case" )
elif(ascii>96 and ascii<123):
    print(char," is an Lower Case" )
else:
    print(char," is not an alphabet" )