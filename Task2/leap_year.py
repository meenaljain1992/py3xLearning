#Create a program that determines whether a given year is a leap year.
#num=2024
#if(num%4==0):
    #print("is a Leap year")
#else:
    #print("is not a Leap year")
num= int(input("Enter a year"))
if(num%4==0 and num%100!=0 or num%400==0 ):
    print("is a leap year")
else:
    print("is not a leap year")