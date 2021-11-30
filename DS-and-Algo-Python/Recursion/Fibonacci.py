def recursive_fibonacci(index):
    if index<=1:
        return index
    return recursive_fibonacci(index-2)+recursive_fibonacci(index-1)

print(recursive_fibonacci(12))

def iterative_fibonacci(index):
    arr=[0,1]
    for i in range(2,index+1):
       arr.append(arr[i-2]+arr[i-1])
    return arr[index]

print(iterative_fibonacci(12))
