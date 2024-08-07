def decor1(func):
    def wrapper():
        print("before")

        func()
        print("after")

    return wrapper

@decor1
def function1():
    sum1= 2+2
    return sum1



result2 = function1()

print(result2)