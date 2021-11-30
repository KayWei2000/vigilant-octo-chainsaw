def naive(array):
    for i in range(0,len(array)):
        for j in range(i+1,len(array)):
            if array[i]==array[j]:
                return array[i]
    return

array = [2,1,1,2,3,4,5]
print(naive(array))

def simple(array):
   dict={} 
   for i in range(0,len(array)):
       if array[i] in dict:
           return array[i]
       else:
           dict[i]=array[i]
   return
print(simple(array))
