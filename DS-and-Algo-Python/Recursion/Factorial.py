def iterative_factorial(number):
    result=1
    for i in range(1,number+1):
        result=result*i
    return result

print(iterative_factorial(5))
    
def recursive_factorial(number):
    if number<=2:
        return number
    return number * recursive_factorial(number-1)

print(recursive_factorial(5))