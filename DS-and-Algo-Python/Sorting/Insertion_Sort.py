def insertionSort(arr): # Especially useful when the array is nearly sorted
    count=0
    for i in range(1,len(arr)):
       key=arr[i]
       j=i-1
       while arr[j]>key and j>=0: # 左边sorted 右边unsorted
            count+=1
            arr[j+1]=arr[j]
            j-=1
       arr[j+1]=key
    return (f'{arr}\nNumber of comparisons = {count}')

array = [5,9,3,10,45,2,0]
print(insertionSort(array))
        
            
           
            

