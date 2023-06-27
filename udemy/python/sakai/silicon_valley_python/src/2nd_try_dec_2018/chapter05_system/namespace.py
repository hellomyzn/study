"""
TEST TEST ##########################
"""

animal = "cat"

def f():
    """TEST unc doc"""
    animal = 'dog'
    print('local :', locals())
    print(f.__name__)
    print(f.__doc__)

f()
print("global:", animal)
print("global:", globals())
print("global:", __name__)
