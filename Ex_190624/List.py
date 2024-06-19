#List nothing but collection of items
numbers = [1,2,3]
def do_something(numbers): # def do_something(meenal) all place in numbers use anything
    numbers.append(4)      # Adding a number
    numbers[0] = 100      # change the value also
    return numbers
l = do_something(numbers)
print(l)