# a=3 # Use as global variable interpreter knows as the value of a
global_a = 4


def f1():
    print(global_a)


f1()
