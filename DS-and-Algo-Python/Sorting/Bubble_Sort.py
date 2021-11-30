def bubble_sort(array):
    count=0
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            count+=1
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return (f'{array}\nNumber of comparisons = {count}')
    
def optimized_bubble_sort(array):
    count=0
    for i in range(len(array)-1):
        swap=False
        for j in range(len(array)-1):
            count+=1
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                swap=True
        if swap==False:
             return(f'{array}\nNumber of comparisons = {count}')
    return(f'{array}\nNumber of comparisons={count}')

array = [5,9,3,10,45,2,0]
print(bubble_sort(array))
print(optimized_bubble_sort(array))
                
    