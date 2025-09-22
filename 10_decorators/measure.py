from time import sleep, time
def measure(func, *args, **kwargs):
    def wrapper(*args,**kwargs):
        t = time() # get current time
        func() # call the received function
        print(func.__name__, "took:", time()-t)
    return wrapper