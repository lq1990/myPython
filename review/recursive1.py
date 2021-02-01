

def fn(string):
    if string == "":
        return string
    return fn(string[1:]) + string[0]


print(fn("hello"))
