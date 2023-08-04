
def print_all_2(*args):
    print(type(args))
    sum = 0
    for i in args:
        sum += 1

def fake_infor(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(f"${i}")