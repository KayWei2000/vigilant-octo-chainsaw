from functools import lru_cache
@lru_cache

def fib(n):
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)

print(fib(10))
print(fib.cache_info())

cache={}    
def fibo(n):
    if n in cache:
        return cache[n]
    elif n<2:
        cache[n]=n
        return cache[n]
    else:
        cache[n]=fibo(n-1)+fibo(n-2)
        return cache[n]
    
print(fibo(8))
print(cache)