# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
num1 = float(input("Enter number first"))
num2 = float(input("Enter number second"))
if (num1 > num2):
    print("num1 is greater")
elif (num2 > num1):
    print("num1 is lesser")
else:
    print("num1 and num2 is equal")
