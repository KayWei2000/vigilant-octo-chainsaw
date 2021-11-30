def add80(n):
    print('Long time')
    return n+80

print(add80(5))
print(add80(5))

# memoization 1
cache={}
def memoizedadd80(n):
    if n in cache:
        return n+80
    else:
        print('long time')
        cache[n]=n+80
        return cache[n]
    
print(memoizedadd80(6))
print(memoizedadd80(6))

# memoization 2
def memoizedadd80():
    cache={}
    
    def memoized(n):
        if n in cache:
            return n+80
        else:
            print('Long time')
            cache[n]=n+80
            return cache[n]
    return memoized

memo=memoizedadd80()
print(memo(7))
print(memo(7))

from functools import lru_cache
@lru_cache()    
def memoized2add80(n):
    return n+80
print(memoized2add80(8))
print(memoized2add80(8))
print(memoized2add80.cache_info())

        