

def validator(func):
    def wrapper(*args, **kwargs):
        print("wrapper started")
        x = func(*args, **kwargs)
        print("wrapper ended")
        return x

    return wrapper()


@validator
def test(x):
    print(x)
    return x



y = test(4)
