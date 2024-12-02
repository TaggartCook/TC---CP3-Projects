def cough(func):
    
    def func_wrapper():
        #stuff that happens before the function
        print("*cough*")
        func()
        #stuff that happens after the function
        print("*cough*")

    return func_wrapper


@cough
def awkward():
    print("Can I get a discount?")


@cough
def answer():
    print("Sir this is a dollar tree. . . ")

awkward()
answer()