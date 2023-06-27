def print_more(func):
    def wrapper(*args, **kwargs):
        print("name: ", func.__name__)
        print("args:", args)
        print("kwargs:", kwargs)
        result = func(*args, **kwargs)
        print("result: ", result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print("start")
        result = func(*args, **kwargs)
        print(result)
        print("end")
        return result
    return wrapper

@print_more
@print_info
def add_num(a, b):
    return a * b

r = add_num(10, 20)
