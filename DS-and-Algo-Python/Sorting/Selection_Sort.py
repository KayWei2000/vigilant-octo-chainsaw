def selection_sort(arr):
    count=0
    for i in range(len(arr)-1):
        min=arr[i]
        for j in range(i+1,len(arr)):
            count+=1
            if arr[j]<min:
                min=arr[j]
                arr[i],arr[j]=arr[j],arr[i]
    return (f'{arr}\nNumber of comparisons = {count}')

arr = [5,9,3,10,45,2,0]
print(selection_sort(arr))