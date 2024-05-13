def positivediff(x, y):
    print(x - y)


def mydecorator(func):
    def inner(x, y):
        if x > y:
            return func(x, y)
        else:
            return func(y, x)
        return inner


result = mydecorator(positivediff(100, 400))

