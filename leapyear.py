year = int(input("enter a year :"))
if (year % 4) == 0:
    #checking if it is century year
   if (year % 100) == 0:
       #century year is leap year only when it is devisible by 400
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
   print("{0} is not a leap year".format(year))