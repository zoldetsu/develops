from datetime import datetime

def timei(arg):
    print(arg)
    def outer(func):
        def wrapper(*args,**kwargs):
            start = datetime.now()
            result = func(*args,**kwargs)
            print(datetime.now() - start)    
            return result
    
        return wrapper
    return outer

@timei('name')
def one(n):
    # start = datetime.now()
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    # print(datetime.now() - start)
    return l
@timei('name')
def two(n):
    # start = datetime.now()
    l = [x for x in range(n) if x % 2 == 0]
    # print(datetime.now() - start)
    return l

l1 = one(10000)
l2 = two(10000)
l3 = timei("name")(one)(10)
# print(l1)
# print(l2)