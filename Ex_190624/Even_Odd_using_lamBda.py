#By using function
def Even_Odd(num):

    if num%2==0:
        print("Even")
    else:
        print("Odd")

check_number = Even_Odd(5)
#By using lamBda
check_number =lambda num : "Even" if num%2==0 else "Odd"
print(check_number(7))