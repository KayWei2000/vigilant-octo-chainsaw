count=0

def mergesort(arr):
    if len(arr)==1:
        return arr
    else:
        mid=len(arr)//2 # rounds down the answer, and returns a whole number
        left=arr[:mid]
        right=arr[mid:] 
        print('left:{}'.format(left))
        print('right:{}'.format(right))
    return merge(mergesort(left),mergesort(right))

def merge(left,right):
    
    sorted_arr=[]
    left_index=0
    right_index=0
    
    while left_index<len(left) and right_index<len(right):
       global count #declare 'count' used in this function is the global one
       count+=1
       if left[left_index]<=right[right_index]:
           sorted_arr.append(left[left_index])
           left_index+=1
       else:
           sorted_arr.append(right[right_index])
           right_index+=1
    print(sorted_arr+left[left_index:]+right[right_index:])
    return sorted_arr+left[left_index:]+right[right_index:]

array = [5,9,3,10,45,2,0]
print(mergesort(array))
print(f'Number of comparisons = {count}')     

        