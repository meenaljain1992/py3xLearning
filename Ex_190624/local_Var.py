# define a local var that is not allow outside the function only inside the function
def my_function():
    a = 10
    local_var =37
    print("Hello")
    print(a)

 #print(a)    Not allowed
my_function()
