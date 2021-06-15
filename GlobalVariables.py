# global variables
    # called from anywhere

# local variables
    # only where declared

x = 100
def check():
    global x
    x = 200
    y = 100
    print(x)
    print(y)

check()
print(x)


def whatever(x):
    if isinstance(x, list):
        x = [5]
    elif isinstance(x, dict):
        x['data'] = 5
    else:
        x = 5
    return x

a = [6]
print(whatever(a), a) #[5], [5], #[5], [5]
b = {}
print(whatever(b), b) #{data:5}, {data:5} #  {} , {}
c = 9
print(whatever(c), c) # 5, 9 # 9, 9







