import time
from wrapper_time import timer



@timer
def func(a: int, b: int):
    time.sleep(2)
    return a + b


print(func(100000, 100000000000))


assert func(5, 5) == 10

